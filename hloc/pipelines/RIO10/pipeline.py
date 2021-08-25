from pathlib import Path

from ... import extract_features, match_features, reconstruction, pairs_from_retrieval



#feature_path = Path(export_dir, feature_conf['output']+'.h5')
#features = feature_conf['output']
#match_path = Path(export_dir, f'{features}_{matcher_conf["output"]}_{sfm_pairs.stem}.h5')

dataset = Path('datasets/RIO10')
images = dataset / 'mapping/sensors/records_data/seq03_01'

query_images = dataset / 'validation/sensors/records_data/seq03_02'
query_list = dataset / 'retrieval.txt'

outputs = Path('outputs/sfm/')
results_path = outputs / 'RIO10SFM_hloc_superpoint+superglue_netvlad40.txt'  # the result file

sfm_pairs = outputs / 'pairs-exhaustive_try2.txt'  # exhaustive matching
sfm_dir = outputs / 'sfm_superpoint+superglue'
num_loc= 1
loc_pairs = outputs / f'pairs-query-netvlad{num_loc}.txt'

feature_conf = extract_features.confs['superpoint_inloc']
matcher_conf = match_features.confs['NN-superpoint']#['superglue']
retrieval_conf = extract_features.confs['netvlad']

#feature_path = extract_features.main(feature_conf, images, outputs, as_half=True)
feature_path = Path(outputs, feature_conf['output']+'.h5')
#match_path = match_features.main(
#    matcher_conf, sfm_pairs, feature_conf['output'], outputs, exhaustive=True)
features = feature_conf['output']
match_path = Path(outputs, f'{features}_{matcher_conf["output"]}_{sfm_pairs.stem}.h5')
#reconstruction.main(sfm_dir, images, sfm_pairs, feature_path, match_path)

#global_descriptors = extract_features.main(retrieval_conf, images, outputs)
global_descriptors = extract_features.main(retrieval_conf, query_images, outputs)

#pairs_from_retrieval.main(global_descriptors, loc_pairs, num_loc, query_list=query_list, db_model=sfm_dir)

features = extract_features.main(
        feature_conf, query_images, outputs, as_half=True)
loc_matches = match_features.main(
        matcher_conf, loc_pairs, feature_conf['output'], outputs)

localize_sfm.main(
    sfm_dir, query_list, sfm_pairs, features , loc_matches, results_path)
