#!/usr/bin/env python


import tensorflow as tf

from tensorflow.contrib import crf

def classification_loss(logits, targets, num_targets, params):
    #squeeze()删除所有尺寸为1的维度，如果设置了squeeze_dim，则只删除其中的维度，如果尺寸非1报错
    #one_hot()将一维的indices数组变成indices_length*num_targets维度的独热编码
    labels = tf.one_hot(tf.squeeze(targets, axis=1), num_targets)
    #使用softmax_cross_entropy时注意logits不用先进行softmax处理
    loss = tf.losses.softmax_cross_entropy(labels, logits, reduction=tf.losses.Reduction.MEAN)
    pred = tf.nn.softmax(logits, name="prediction")
    tf.summary.scalar("loss", loss)
    tf.summary.histogram("pred", tf.argmax(pred, axis=-1))

    return loss, pred
