[2018-10-22 20:51:54] load data ...
X.shape:  (2050, 500)
y.shape:  (2050,)
[2018-10-22 20:51:55] train model ...
============================= train _K_ flod 0 ====================================
[LightGBM] [Warning] Starting from the 2.1.2 version, default value for the "boost_from_average" parameter in "binary" objective is true.
This may cause significantly different results comparing to the previous versions of LightGBM.
Try to set boost_from_average=false, if your old models produce bad results
[LightGBM] [Info] Number of positive: 600, number of negative: 1039
[LightGBM] [Info] Total Bins 37160
[LightGBM] [Info] Number of data: 1639, number of used features: 500
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.366077 -> initscore=-0.549084
[LightGBM] [Info] Start training from score -0.549084
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
/home/k/.conda/envs/python35/lib/python3.5/site-packages/sklearn/metrics/classification.py:1135: UndefinedMetricWarning: F-score is ill-defined and being set to 0.0 due to no predicted samples.
  'precision', 'predicted', average, warn_for)
Training until validation scores don't improve for 50 rounds.
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[10]	valid_0's binary_logloss: 0.353978	valid_0's f1_score: 0.966887
[20]	valid_0's binary_logloss: 0.219715	valid_0's f1_score: 0.966887
[30]	valid_0's binary_logloss: 0.149218	valid_0's f1_score: 0.966887
[40]	valid_0's binary_logloss: 0.109189	valid_0's f1_score: 0.964401
[50]	valid_0's binary_logloss: 0.0865274	valid_0's f1_score: 0.970297
[60]	valid_0's binary_logloss: 0.0743144	valid_0's f1_score: 0.97351
[70]	valid_0's binary_logloss: 0.0680114	valid_0's f1_score: 0.966887
[80]	valid_0's binary_logloss: 0.0653294	valid_0's f1_score: 0.967105
[90]	valid_0's binary_logloss: 0.0670771	valid_0's f1_score: 0.967105
[100]	valid_0's binary_logloss: 0.0706104	valid_0's f1_score: 0.96732
Early stopping, best iteration is:
[56]	valid_0's binary_logloss: 0.0790633	valid_0's f1_score: 0.97351
best_iteration:  56
valid_f1_score:  0.973509933775
============================= train _K_ flod 1 ====================================
[LightGBM] [Warning] Starting from the 2.1.2 version, default value for the "boost_from_average" parameter in "binary" objective is true.
This may cause significantly different results comparing to the previous versions of LightGBM.
Try to set boost_from_average=false, if your old models produce bad results
[LightGBM] [Info] Number of positive: 601, number of negative: 1039
[LightGBM] [Info] Total Bins 37072
[LightGBM] [Info] Number of data: 1640, number of used features: 500
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.366463 -> initscore=-0.547419
[LightGBM] [Info] Start training from score -0.547419
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
Training until validation scores don't improve for 50 rounds.
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[10]	valid_0's binary_logloss: 0.345613	valid_0's f1_score: 0.983389
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[20]	valid_0's binary_logloss: 0.204133	valid_0's f1_score: 0.977049
[30]	valid_0's binary_logloss: 0.129537	valid_0's f1_score: 0.977049
[40]	valid_0's binary_logloss: 0.0880416	valid_0's f1_score: 0.973684
[50]	valid_0's binary_logloss: 0.0636115	valid_0's f1_score: 0.976744
Early stopping, best iteration is:
[2]	valid_0's binary_logloss: 0.568398	valid_0's f1_score: 0.986486
best_iteration:  2
valid_f1_score:  0.986486486486
============================= train _K_ flod 2 ====================================
[LightGBM] [Warning] Starting from the 2.1.2 version, default value for the "boost_from_average" parameter in "binary" objective is true.
This may cause significantly different results comparing to the previous versions of LightGBM.
Try to set boost_from_average=false, if your old models produce bad results
[LightGBM] [Info] Number of positive: 601, number of negative: 1039
[LightGBM] [Info] Total Bins 37145
[LightGBM] [Info] Number of data: 1640, number of used features: 500
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.366463 -> initscore=-0.547419
[LightGBM] [Info] Start training from score -0.547419
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
Training until validation scores don't improve for 50 rounds.
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[10]	valid_0's binary_logloss: 0.356466	valid_0's f1_score: 0.963211
[20]	valid_0's binary_logloss: 0.221986	valid_0's f1_score: 0.955932
[30]	valid_0's binary_logloss: 0.151283	valid_0's f1_score: 0.959184
[40]	valid_0's binary_logloss: 0.111268	valid_0's f1_score: 0.95302
[50]	valid_0's binary_logloss: 0.0890286	valid_0's f1_score: 0.95302
[60]	valid_0's binary_logloss: 0.0813098	valid_0's f1_score: 0.95302
Early stopping, best iteration is:
[12]	valid_0's binary_logloss: 0.321254	valid_0's f1_score: 0.967532
best_iteration:  12
valid_f1_score:  0.967532467532
============================= train _K_ flod 3 ====================================
[LightGBM] [Warning] Starting from the 2.1.2 version, default value for the "boost_from_average" parameter in "binary" objective is true.
This may cause significantly different results comparing to the previous versions of LightGBM.
Try to set boost_from_average=false, if your old models produce bad results
[LightGBM] [Info] Number of positive: 601, number of negative: 1039
[LightGBM] [Info] Total Bins 37196
[LightGBM] [Info] Number of data: 1640, number of used features: 500
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.366463 -> initscore=-0.547419
[LightGBM] [Info] Start training from score -0.547419
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
Training until validation scores don't improve for 50 rounds.
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[10]	valid_0's binary_logloss: 0.347703	valid_0's f1_score: 0.970874
[20]	valid_0's binary_logloss: 0.207515	valid_0's f1_score: 0.970874
[30]	valid_0's binary_logloss: 0.133977	valid_0's f1_score: 0.970874
[40]	valid_0's binary_logloss: 0.092905	valid_0's f1_score: 0.964169
[50]	valid_0's binary_logloss: 0.0684539	valid_0's f1_score: 0.964169
Early stopping, best iteration is:
[5]	valid_0's binary_logloss: 0.466989	valid_0's f1_score: 0.980132
best_iteration:  5
valid_f1_score:  0.980132450331
============================= train _K_ flod 4 ====================================
[LightGBM] [Warning] Starting from the 2.1.2 version, default value for the "boost_from_average" parameter in "binary" objective is true.
This may cause significantly different results comparing to the previous versions of LightGBM.
Try to set boost_from_average=false, if your old models produce bad results
[LightGBM] [Info] Number of positive: 601, number of negative: 1040
[LightGBM] [Info] Total Bins 37221
[LightGBM] [Info] Number of data: 1641, number of used features: 500
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.366240 -> initscore=-0.548381
[LightGBM] [Info] Start training from score -0.548381
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
Training until validation scores don't improve for 50 rounds.
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[10]	valid_0's binary_logloss: 0.355865	valid_0's f1_score: 0.963455
[20]	valid_0's binary_logloss: 0.220793	valid_0's f1_score: 0.960784
[30]	valid_0's binary_logloss: 0.152602	valid_0's f1_score: 0.966887
[40]	valid_0's binary_logloss: 0.115694	valid_0's f1_score: 0.966887
[50]	valid_0's binary_logloss: 0.0973116	valid_0's f1_score: 0.966887
Early stopping, best iteration is:
[2]	valid_0's binary_logloss: 0.571299	valid_0's f1_score: 0.969283
best_iteration:  2
valid_f1_score:  0.969283276451
train_logloss:  0.401400460232
test_logloss:  0.02
[('num', 0), ('score_3', 0), ('score_5', 0), ('score_6', 0), ('score_7', 0), ('score_8', 0), ('score_9', 0), ('score_10', 0), ('prefix_len', 0), ('prefix_uniq_len', 0), ('prefix_seg_len', 0), ('prefix_skew', 0), ('prefix_kurtosis', 0), ('title_len', 0), ('title_uniq_len', 0), ('title_seg_len', 0), ('title_skew', 0), ('text_1_len', 0), ('text_1_uniq_len', 0), ('text_1_seg_len', 0), ('text_1_skew', 0), ('text_1_kurtosis', 0), ('text_2_len', 0), ('text_2_uniq_len', 0), ('text_2_seg_len', 0), ('text_2_skew', 0), ('text_2_kurtosis', 0), ('text_3_len', 0), ('text_3_uniq_len', 0), ('text_3_seg_len', 0), ('text_3_skew', 0), ('text_3_kurtosis', 0), ('text_4_len', 0), ('text_4_uniq_len', 0), ('text_4_seg_len', 0), ('text_4_skew', 0), ('text_4_kurtosis', 0), ('text_5_len', 0), ('text_5_uniq_len', 0), ('text_5_seg_len', 0), ('text_5_skew', 0), ('text_5_kurtosis', 0), ('text_6_len', 0), ('text_6_uniq_len', 0), ('text_6_seg_len', 0), ('text_6_skew', 0), ('text_6_kurtosis', 0), ('text_7_len', 0), ('text_7_uniq_len', 0), ('text_7_seg_len', 0), ('text_7_skew', 0), ('text_7_kurtosis', 0), ('text_8_len', 0), ('text_8_uniq_len', 0), ('text_8_seg_len', 0), ('text_8_skew', 0), ('text_8_kurtosis', 0), ('text_9_len', 0), ('text_9_uniq_len', 0), ('text_9_seg_len', 0), ('text_9_skew', 0), ('text_9_kurtosis', 0), ('text_10_len', 0), ('text_10_uniq_len', 0), ('text_10_seg_len', 0), ('text_10_skew', 0), ('text_10_kurtosis', 0), ('prefix_title_diff_len', 0), ('prefix_title_common_seg', 0), ('prefix_title_cosine_distance', 0), ('prefix_title_jaccard_distance', 0), ('prefix_title_cityblock_distance', 0), ('prefix_title_canberra_distance', 0), ('prefix_title_euclidean_distance', 0), ('prefix_title_minkowski_distance', 0), ('prefix_title_braycurtis_distance', 0), ('text_1_title_diff_len', 0), ('text_1_title_common_seg', 0), ('text_1_title_cosine_distance', 0), ('text_1_title_jaccard_distance', 0), ('text_1_title_cityblock_distance', 0), ('text_1_title_canberra_distance', 0), ('text_1_title_euclidean_distance', 0), ('text_1_title_minkowski_distance', 0), ('text_1_title_braycurtis_distance', 0), ('text_2_title_diff_len', 0), ('text_2_title_common_seg', 0), ('text_2_title_cosine_distance', 0), ('text_2_title_jaccard_distance', 0), ('text_2_title_cityblock_distance', 0), ('text_2_title_canberra_distance', 0), ('text_2_title_euclidean_distance', 0), ('text_2_title_minkowski_distance', 0), ('text_2_title_braycurtis_distance', 0), ('text_3_title_diff_len', 0), ('text_3_title_common_seg', 0), ('text_3_title_cosine_distance', 0), ('text_3_title_jaccard_distance', 0), ('text_3_title_cityblock_distance', 0), ('text_3_title_canberra_distance', 0), ('text_3_title_euclidean_distance', 0), ('text_3_title_minkowski_distance', 0), ('text_3_title_braycurtis_distance', 0), ('text_4_title_diff_len', 0), ('text_4_title_common_seg', 0), ('text_4_title_cosine_distance', 0), ('text_4_title_jaccard_distance', 0), ('text_4_title_cityblock_distance', 0), ('text_4_title_canberra_distance', 0), ('text_4_title_euclidean_distance', 0), ('text_4_title_minkowski_distance', 0), ('text_4_title_braycurtis_distance', 0), ('text_5_title_diff_len', 0), ('text_5_title_common_seg', 0), ('text_5_title_cosine_distance', 0), ('text_5_title_jaccard_distance', 0), ('text_5_title_cityblock_distance', 0), ('text_5_title_canberra_distance', 0), ('text_5_title_euclidean_distance', 0), ('text_5_title_minkowski_distance', 0), ('text_5_title_braycurtis_distance', 0), ('text_6_title_diff_len', 0), ('text_6_title_common_seg', 0), ('text_6_title_cosine_distance', 0), ('text_6_title_jaccard_distance', 0), ('text_6_title_cityblock_distance', 0), ('text_6_title_canberra_distance', 0), ('text_6_title_euclidean_distance', 0), ('text_6_title_minkowski_distance', 0), ('text_6_title_braycurtis_distance', 0), ('text_7_title_diff_len', 0), ('text_7_title_common_seg', 0), ('text_7_title_cosine_distance', 0), ('text_7_title_jaccard_distance', 0), ('text_7_title_cityblock_distance', 0), ('text_7_title_canberra_distance', 0), ('text_7_title_euclidean_distance', 0), ('text_7_title_minkowski_distance', 0), ('text_7_title_braycurtis_distance', 0), ('text_8_title_diff_len', 0), ('text_8_title_common_seg', 0), ('text_8_title_cosine_distance', 0), ('text_8_title_jaccard_distance', 0), ('text_8_title_cityblock_distance', 0), ('text_8_title_canberra_distance', 0), ('text_8_title_euclidean_distance', 0), ('text_8_title_minkowski_distance', 0), ('text_8_title_braycurtis_distance', 0), ('text_9_title_diff_len', 0), ('text_9_title_common_seg', 0), ('text_9_title_cosine_distance', 0), ('text_9_title_jaccard_distance', 0), ('text_9_title_cityblock_distance', 0), ('text_9_title_canberra_distance', 0), ('text_9_title_euclidean_distance', 0), ('text_9_title_minkowski_distance', 0), ('text_9_title_braycurtis_distance', 0), ('text_10_title_diff_len', 0), ('text_10_title_common_seg', 0), ('text_10_title_cosine_distance', 0), ('text_10_title_jaccard_distance', 0), ('text_10_title_cityblock_distance', 0), ('text_10_title_canberra_distance', 0), ('text_10_title_euclidean_distance', 0), ('text_10_title_minkowski_distance', 0), ('text_10_title_braycurtis_distance', 0), ('prefix_title_word_match_share', 0), ('prefix_title_tfidf_word_match_share', 0), ('prefix_title_tfidf_word_match_share_stops', 0), ('prefix_title_jaccard', 0), ('prefix_title_wc_ratio', 0), ('prefix_title_wc_ratio_unique', 0), ('prefix_title_wc_ratio_unique_stop', 0), ('prefix_title_same_start', 0), ('prefix_title_char_diff', 0), ('prefix_title_char_diff_unique_stop', 0), ('prefix_title_total_unique_words', 0), ('prefix_title_total_unq_words_stop', 0), ('prefix_title_char_ratio', 0), ('text_1_title_word_match_share', 0), ('text_1_title_tfidf_word_match_share', 0), ('text_1_title_tfidf_word_match_share_stops', 0), ('text_1_title_jaccard', 0), ('text_1_title_wc_ratio', 0), ('text_1_title_wc_ratio_unique', 0), ('text_1_title_wc_ratio_unique_stop', 0), ('text_1_title_same_start', 0), ('text_1_title_char_diff', 0), ('text_1_title_char_diff_unique_stop', 0), ('text_1_title_total_unique_words', 0), ('text_1_title_total_unq_words_stop', 0), ('text_1_title_char_ratio', 0), ('text_2_title_word_match_share', 0), ('text_2_title_tfidf_word_match_share', 0), ('text_2_title_tfidf_word_match_share_stops', 0), ('text_2_title_jaccard', 0), ('text_2_title_wc_ratio', 0), ('text_2_title_wc_ratio_unique', 0), ('text_2_title_wc_ratio_unique_stop', 0), ('text_2_title_same_start', 0), ('text_2_title_char_diff', 0), ('text_2_title_char_diff_unique_stop', 0), ('text_2_title_total_unique_words', 0), ('text_2_title_total_unq_words_stop', 0), ('text_2_title_char_ratio', 0), ('text_3_title_word_match_share', 0), ('text_3_title_tfidf_word_match_share', 0), ('text_3_title_tfidf_word_match_share_stops', 0), ('text_3_title_jaccard', 0), ('text_3_title_wc_ratio', 0), ('text_3_title_wc_ratio_unique', 0), ('text_3_title_wc_ratio_unique_stop', 0), ('text_3_title_same_start', 0), ('text_3_title_char_diff', 0), ('text_3_title_char_diff_unique_stop', 0), ('text_3_title_total_unique_words', 0), ('text_3_title_total_unq_words_stop', 0), ('text_3_title_char_ratio', 0), ('text_4_title_word_match_share', 0), ('text_4_title_tfidf_word_match_share', 0), ('text_4_title_tfidf_word_match_share_stops', 0), ('text_4_title_jaccard', 0), ('text_4_title_wc_ratio', 0), ('text_4_title_wc_ratio_unique', 0), ('text_4_title_wc_ratio_unique_stop', 0), ('text_4_title_same_start', 0), ('text_4_title_char_diff', 0), ('text_4_title_char_diff_unique_stop', 0), ('text_4_title_total_unique_words', 0), ('text_4_title_total_unq_words_stop', 0), ('text_4_title_char_ratio', 0), ('text_5_title_word_match_share', 0), ('text_5_title_tfidf_word_match_share', 0), ('text_5_title_tfidf_word_match_share_stops', 0), ('text_5_title_jaccard', 0), ('text_5_title_wc_ratio', 0), ('text_5_title_wc_ratio_unique', 0), ('text_5_title_wc_ratio_unique_stop', 0), ('text_5_title_same_start', 0), ('text_5_title_char_diff', 0), ('text_5_title_char_diff_unique_stop', 0), ('text_5_title_total_unique_words', 0), ('text_5_title_total_unq_words_stop', 0), ('text_5_title_char_ratio', 0), ('text_6_title_word_match_share', 0), ('text_6_title_tfidf_word_match_share', 0), ('text_6_title_tfidf_word_match_share_stops', 0), ('text_6_title_jaccard', 0), ('text_6_title_wc_ratio', 0), ('text_6_title_wc_ratio_unique', 0), ('text_6_title_wc_ratio_unique_stop', 0), ('text_6_title_same_start', 0), ('text_6_title_char_diff', 0), ('text_6_title_char_diff_unique_stop', 0), ('text_6_title_total_unique_words', 0), ('text_6_title_total_unq_words_stop', 0), ('text_6_title_char_ratio', 0), ('text_7_title_word_match_share', 0), ('text_7_title_tfidf_word_match_share', 0), ('text_7_title_tfidf_word_match_share_stops', 0), ('text_7_title_jaccard', 0), ('text_7_title_wc_ratio', 0), ('text_7_title_wc_ratio_unique', 0), ('text_7_title_wc_ratio_unique_stop', 0), ('text_7_title_same_start', 0), ('text_7_title_char_diff', 0), ('text_7_title_char_diff_unique_stop', 0), ('text_7_title_total_unique_words', 0), ('text_7_title_total_unq_words_stop', 0), ('text_7_title_char_ratio', 0), ('text_8_title_word_match_share', 0), ('text_8_title_tfidf_word_match_share', 0), ('text_8_title_tfidf_word_match_share_stops', 0), ('text_8_title_jaccard', 0), ('text_8_title_wc_ratio', 0), ('text_8_title_wc_ratio_unique', 0), ('text_8_title_wc_ratio_unique_stop', 0), ('text_8_title_same_start', 0), ('text_8_title_char_diff', 0), ('text_8_title_char_diff_unique_stop', 0), ('text_8_title_total_unique_words', 0), ('text_8_title_total_unq_words_stop', 0), ('text_8_title_char_ratio', 0), ('text_9_title_word_match_share', 0), ('text_9_title_tfidf_word_match_share', 0), ('text_9_title_tfidf_word_match_share_stops', 0), ('text_9_title_jaccard', 0), ('text_9_title_wc_ratio', 0), ('text_9_title_wc_ratio_unique', 0), ('text_9_title_wc_ratio_unique_stop', 0), ('text_9_title_same_start', 0), ('text_9_title_char_diff', 0), ('text_9_title_char_diff_unique_stop', 0), ('text_9_title_total_unique_words', 0), ('text_9_title_total_unq_words_stop', 0), ('text_9_title_char_ratio', 0), ('text_10_title_word_match_share', 0), ('text_10_title_tfidf_word_match_share', 0), ('text_10_title_tfidf_word_match_share_stops', 0), ('text_10_title_jaccard', 0), ('text_10_title_wc_ratio', 0), ('text_10_title_wc_ratio_unique', 0), ('text_10_title_wc_ratio_unique_stop', 0), ('text_10_title_same_start', 0), ('text_10_title_char_diff', 0), ('text_10_title_char_diff_unique_stop', 0), ('text_10_title_total_unique_words', 0), ('text_10_title_total_unq_words_stop', 0), ('text_10_title_char_ratio', 0), ('prefix_click', 0), ('prefix_show', 0), ('prefix_ctr', 0), ('title_show', 0), ('title_click', 0), ('title_ctr', 0), ('tag_show', 0), ('tag_click', 0), ('tag_ctr', 0), ('prefix_title_show', 0), ('prefix_title_click', 0), ('prefix_title_ctr', 0), ('prefix_tag_click', 0), ('title_tag_click', 0), ('title_tag_show', 0), ('title_tag_ctr', 0), ('text_1_click', 0), ('text_1_show', 0), ('text_1_ctr', 0), ('text_2_click', 0), ('text_2_show', 0), ('text_2_ctr', 0), ('text_3_show', 0), ('text_3_ctr', 0), ('text_4_click', 0), ('text_4_ctr', 0), ('text_5_click', 0), ('text_5_show', 0), ('text_5_ctr', 0), ('text_6_click', 0), ('text_6_show', 0), ('text_6_ctr', 0), ('text_7_show', 0), ('text_7_click', 0), ('text_7_ctr', 0), ('text_8_show', 0), ('text_8_click', 0), ('text_8_ctr', 0), ('text_9_click', 0), ('text_9_show', 0), ('text_9_ctr', 0), ('text_10_show', 0), ('text_10_click', 0), ('text_10_ctr', 0), ('text_1_text_2_click', 0), ('text_1_text_2_ctr', 0), ('text_1_text_3_click', 0), ('text_1_text_3_show', 0), ('text_1_text_4_click', 0), ('text_1_text_4_show', 0), ('text_1_text_4_ctr', 0), ('text_1_text_5_click', 0), ('text_1_text_5_show', 0), ('text_1_text_5_ctr', 0), ('text_1_text_6_click', 0), ('text_1_text_6_show', 0), ('text_1_text_6_ctr', 0), ('text_1_text_7_click', 0), ('text_1_text_7_show', 0), ('text_1_text_7_ctr', 0), ('text_1_text_8_click', 0), ('text_1_text_8_show', 0), ('text_1_text_8_ctr', 0), ('text_1_text_9_click', 0), ('text_1_text_9_show', 0), ('text_1_text_9_ctr', 0), ('text_1_text_10_show', 0), ('text_1_text_10_click', 0), ('text_1_text_10_ctr', 0), ('text_2_text_3_click', 0), ('text_2_text_3_show', 0), ('text_2_text_3_ctr', 0), ('text_2_text_4_click', 0), ('text_2_text_4_show', 0), ('text_2_text_4_ctr', 0), ('text_2_text_5_click', 0), ('text_2_text_5_show', 0), ('text_2_text_5_ctr', 0), ('text_2_text_6_click', 0), ('text_2_text_6_show', 0), ('text_2_text_6_ctr', 0), ('text_2_text_7_click', 0), ('text_2_text_7_show', 0), ('text_2_text_7_ctr', 0), ('text_2_text_8_show', 0), ('text_2_text_8_click', 0), ('text_2_text_8_ctr', 0), ('text_2_text_9_click', 0), ('text_2_text_9_show', 0), ('text_2_text_9_ctr', 0), ('text_2_text_10_click', 0), ('text_2_text_10_show', 0), ('text_2_text_10_ctr', 0), ('text_3_text_4_click', 0), ('text_3_text_4_show', 0), ('text_3_text_4_ctr', 0), ('text_3_text_5_click', 0), ('text_3_text_5_show', 0), ('text_3_text_5_ctr', 0), ('text_3_text_6_click', 0), ('text_3_text_6_show', 0), ('text_3_text_6_ctr', 0), ('text_3_text_7_click', 0), ('text_3_text_7_show', 0), ('text_3_text_7_ctr', 0), ('text_3_text_8_click', 0), ('text_3_text_8_show', 0), ('text_3_text_8_ctr', 0), ('text_3_text_9_show', 0), ('text_3_text_9_click', 0), ('text_3_text_9_ctr', 0), ('text_3_text_10_show', 0), ('text_3_text_10_click', 0), ('text_3_text_10_ctr', 0), ('text_4_text_5_show', 0), ('text_4_text_5_click', 0), ('text_4_text_5_ctr', 0), ('text_4_text_6_show', 0), ('text_4_text_6_click', 0), ('text_4_text_6_ctr', 0), ('text_4_text_7_show', 0), ('text_4_text_7_click', 0), ('text_4_text_7_ctr', 0), ('text_4_text_8_show', 0), ('text_4_text_8_click', 0), ('text_4_text_8_ctr', 0), ('text_4_text_9_click', 0), ('text_4_text_9_show', 0), ('text_4_text_9_ctr', 0), ('text_4_text_10_click', 0), ('text_4_text_10_show', 0), ('text_4_text_10_ctr', 0), ('text_5_text_6_click', 0), ('text_5_text_6_show', 0), ('text_5_text_6_ctr', 0), ('text_5_text_7_show', 0), ('text_5_text_7_click', 0), ('text_5_text_7_ctr', 0), ('text_5_text_8_show', 0), ('text_5_text_8_click', 0), ('text_5_text_8_ctr', 0), ('text_5_text_9_show', 0), ('text_5_text_9_click', 0), ('text_5_text_9_ctr', 0), ('text_5_text_10_click', 0), ('text_5_text_10_show', 0), ('text_5_text_10_ctr', 0), ('text_6_text_7_show', 0), ('text_6_text_7_click', 0), ('text_6_text_7_ctr', 0), ('text_6_text_8_click', 0), ('text_6_text_8_show', 0), ('text_6_text_8_ctr', 0), ('text_6_text_9_show', 0), ('text_6_text_9_click', 0), ('text_6_text_9_ctr', 0), ('text_6_text_10_show', 0), ('text_6_text_10_click', 0), ('text_6_text_10_ctr', 0), ('text_7_text_8_show', 0), ('text_7_text_8_click', 0), ('text_7_text_8_ctr', 0), ('text_7_text_9_show', 0), ('text_7_text_9_click', 0), ('text_7_text_9_ctr', 0), ('text_7_text_10_click', 0), ('text_7_text_10_show', 0), ('text_7_text_10_ctr', 0), ('text_8_text_9_click', 0), ('text_8_text_9_show', 0), ('text_8_text_9_ctr', 0), ('text_8_text_10_click', 0), ('text_8_text_10_show', 0), ('text_8_text_10_ctr', 0), ('text_9_text_10_click', 0), ('text_9_text_10_show', 0), ('text_9_text_10_ctr', 0), ('score_1', 1), ('score_2', 1), ('score_4', 1), ('title_kurtosis', 1), ('prefix_tag_show', 1), ('prefix_title_tag_click', 1), ('prefix_title_tag_show', 1), ('text_3_click', 1), ('text_4_show', 1), ('text_1_text_2_show', 1), ('text_1_text_3_ctr', 1), ('prefix_tag_ctr', 2), ('prefix_title_tag_ctr', 2), ('tag', 3)]
[2018-10-22 20:51:56] done ...
