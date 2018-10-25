
expname = "classification"


MAX_QUERY_NUM = 14

# 设置为"test_A"或者"test_B"
data_type = "test_A"

#原始数据
ORI_TRAIN_DATA_FILE = "/home/k/PycharmProjects/data/OGeek/oppo_round1_train_20180929.txt"
ORI_VALID_DATA_FILE = "/home/k/PycharmProjects/data/OGeek/oppo_round1_vali_20180929.txt"
ORI_TEST_DATA_FILE = "/home/k/PycharmProjects/data/OGeek/oppo_round1_test_A_20180929.txt"
ORI_TEST_B_DATA_FILE = "/home/k/PycharmProjects/data/OGeek/oppo_round1_test_B_20180929.txt"

# 原始的数据预处理后
TRAIN_DATA_FILE = "/home/k/PycharmProjects/data/OGeek/train.txt"
VALID_DATA_FILE = "/home/k/PycharmProjects/data/OGeek/valid.txt"
TEST_DATA_FILE = "/home/k/PycharmProjects/data/OGeek/test.txt"
TEST_B_DATA_FILE = "/home/k/PycharmProjects/data/OGeek/testB.txt"

# 将原来的train和valid合并为train，原来的test用来predict
TRAIN_DATA = "/home/k/PycharmProjects/data/OGeek/final/train.txt"
PREDICT_DATA = "/home/k/PycharmProjects/data/OGeek/final/predict.txt"


#mini的原始数据
MINI_ORI_TRAIN_DATA_FILE = "./data/download/mini_data/oppo_round1_train_20180929.txt"
MINI_ORI_VALID_DATA_FILE = "./data/download/mini_data/oppo_round1_vali_20180929.txt"
MINI_ORI_TEST_DATA_FILE = "./data/download/mini_data/oppo_round1_test_A_20180929.txt"
MINI_ORI_TEST_B_DATA_FILE = "./data/download/mini_data/oppo_round1_test_B_20180929.txt"

# 原始的数据预处理后
MINI_TRAIN_DATA_FILE = "./data/download/mini_data/train.txt"
MINI_VALID_DATA_FILE = "./data/download/mini_data/valid.txt"
MINI_TEST_DATA_FILE = "./data/download/mini_data/test.txt"
MINI_TEST_B_DATA_FILE = "./data/download/mini_data/testB.txt"

# 将原来的train和valid合并为train，原来的test用来predict
MINI_TRAIN_DATA = "./data/train.txt"
MINI_PREDICT_DATA = "./data/predict.txt"


'''
    "train_data": MINI_TRAIN_DATA,
    "predict_data": MINI_PREDICT_DATA,
'''

params = {
    "train_data": TRAIN_DATA,
    "predict_data": PREDICT_DATA,
    "dictionary_path": "./output/dictionary",
    "model_path": "./output/model",
    "train_summary_path": "./output/summary",
    "eval_summary_path": "./output/eval",
    "train_epoch": 10,
    "batch_size": 64,
    "shuffle": False,
    "dictionary_cutoff": 0,
    #???
    "num_targets": 2,
    "word_embedding_dim": 200,
    "is_use_pretrained_word_embedding": False,
    "pretrained_emnedding_dir": "./data/word_vectors.txt",
    "tag_embedding_dim": 4,
    "keep_prob": 0.5,
    "cnn_layers": {
        "filter_width": 3,
        "output_channel": 64,
    },
    "gru_layers": {
        "gru_size": 64,
        "attention_size": 32,
    },
    "dense_layers": [
       {"hidden_units": 128},
       {"hidden_units": 64},
    ],

    "optimizer_type": "adam",
    "learning_rate": 0.003,
    "lr_decay": 1,
    "lr_decay_steps": 10,
    "clip": 0.2,

    #就是说每运行一次，处理的batch数目
    "steps_per_run": 10,
}
