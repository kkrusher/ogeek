#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#
# @Author: yangxiaohan
# @Date: 2018-10-10
#

import os
import sys
import time
from datetime import timedelta
import logging

import numpy as np
import tensorflow as tf

from PIL import Image

sys.path.append("src")
from input import *
from model import Model
from sklearn.metrics import f1_score


sys.path.append("conf")
import config

logging.basicConfig(
        level = logging.INFO, 
        format = "[%(asctime)s] %(message)s",
        datefmt = "%Y-%m-%d %H:%M:%S",
        )



def train(fully = False):
    train_set, valid_set = load_data(config.params["train_data"])
    dictionary = Dictionary(config.params, train_set)
    dictionary.save(config.params["dictionary_path"])
    pad_id = dictionary.pad_id()
    print ("pad_id: ", pad_id)
    vocab_size = dictionary.vocab_size()
    print ("vocab_size: ", vocab_size)
    
    train_set = dictionary.to_id(train_set)
    valid_set = dictionary.to_id(valid_set)
    
    train_bm = BatchManager(train_set, 1, config.params, pad_id)
    valid_bm = BatchManager(valid_set, 1, config.params, pad_id)
    
    model = Model(config.params, vocab_size, dictionary)
    merge_summary = tf.summary.merge_all()
    

    def metrics(targets, preds):
        preds = [int(i[1]>=0.5) for i in preds]
        return f1_score(targets, preds), ""

    
    def get_time_dif(start_time):
        end_time = time.time()
        time_dif = end_time - start_time
        return timedelta(seconds=int(round(time_dif)))
    
    
    summary_path = os.path.join(config.params["train_summary_path"], config.expname)
    os.system("rm -rf %s" % summary_path)
    model_path = os.path.join(config.params["model_path"], config.expname)
    os.system("rm -rf %s" % model_path)
    eval_summary_path = os.path.join(config.params["eval_summary_path"], config.expname)
    os.system("rm -rf %s" % eval_summary_path)
    os.system("mkdir -p %s" % eval_summary_path)
    
    train_writer = tf.summary.FileWriter(summary_path, tf.get_default_graph())
    
    with tf.Session() as sess:
        initializer = tf.global_variables_initializer()
        sess.run(initializer)
        steps_per_run = config.params["steps_per_run"]
        global_step = 0
        best_accuracy = 0.
        start_time = time.time()
        valid_step = 0
        for epoch in range(config.params["train_epoch"]):
            train_bm.init()
            while True:
                global_step, loss, n_steps, (accuracy, _) = model.train(sess, train_bm, steps_per_run, metrics, 
                        merge_summary=merge_summary, train_writer=train_writer)
                logging.info("TRAIN %d steps[%d]: loss %.4f  accuracy %.4f" % (global_step, epoch, loss, accuracy))
                if train_bm.is_finished:
                    break
                
                valid_step += 1
                if valid_step % 5 == 0:
                    valid_bm.init()
                    loss, (accuracy, confusion_matrix) = model.eval(sess, valid_bm, metrics)
                    if accuracy > best_accuracy:
                        best_accuracy = accuracy
                        model.save(sess, save_path=model_path)
                        best_flag = '*'
                    else:
                        best_flag = ''
                    
                    time_dif = get_time_dif(start_time)
                    logging.info("EVALUATION: %d steps: loss %.4f  accuracy %.4f  cost_time %s  %s" % (global_step, loss, accuracy, str(time_dif), best_flag))
    

def predict():
    class Model:
        def __init__(self, params):
            self.type_of_tags = ["prefix", "title", "segments", "tag", "scores", "texts"]
            graph = tf.Graph()
            with graph.as_default():
                self.sess = tf.Session()
                with self.sess.as_default():
                    save_path = params["model_path"] + "/" + config.expname
                    saver = tf.train.import_meta_graph("%s.meta" % save_path)
                    saver.restore(self.sess, save_path)
                    
                    # placeholder
                    type_of_tags = ["prefix", "title", "segments", "tag", "scores", "texts"]
                    self.inputs = {
                        tt: graph.get_operation_by_name(tt).outputs[0] for tt in type_of_tags
                    }

                    self.keep_prob = graph.get_operation_by_name("keep_prob").outputs[0]
                    self.prediction = graph.get_operation_by_name("prediction").outputs[0]


        def predict(self, batch):
            feed_dict = {
                self.inputs[tt]: batch[tt]
                for tt in self.inputs
            }
            feed_dict[self.keep_prob] = 1

            pred = self.sess.run(self.prediction, feed_dict=feed_dict)

            return pred

    config.params["batch_size"] = 1024
    predict_set = load_data(config.params["predict_data"], is_train=0)
    dictionary = Dictionary(config.params, path=config.params["dictionary_path"])
    pad_id = dictionary.pad_id()
    
    predict_set = dictionary.to_id(predict_set)
    predict_bm = BatchManager(predict_set, 1, config.params, pad_id)
    
    model = Model(config.params)
    predict_bm.init()
    with open("./output/result.csv", "w") as f:
        while True:
            batch, batch_size = predict_bm.batch()
            preds = model.predict(batch)
            for pred in preds:
                f.write(str(int(pred[1] >= 0.5)))
                f.write("\n")

            if predict_bm.is_finished:
                break
    

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ["train", "pred", "fully_train"]:
        raise ValueError("""usage: python run_model.py [train / pred]""")

    if sys.argv[1] == "train":
        train(fully = False)
    elif sys.argv[1] == "fully_train":
        train(fully = True)
    else:
        predict()



