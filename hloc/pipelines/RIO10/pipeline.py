from pathlib import Path

from ... import extract_features, match_features, reconstruction

dataset = Path('datasets/RIO10')
images = dataset / 'mapping/sensors/records_data/seq03_01'

outputs = Path('outputs/sfm/')
sfm_pairs = outputs / 'pairs-exhaustive.txt'  # exhaustive matching
sfm_dir = outputs / 'sfm_superpoint+superglue'

feature_conf = extract_features.confs['superpoint_aachen']
matcher_conf = match_features.confs['superglue']

feature_path = extract_features.main(feature_conf, images, outputs)

match_path = match_features.main(
    matcher_conf, sfm_pairs, feature_conf['output'], outputs, exhaustive=True)

reconstruction.main(sfm_dir, images, sfm_pairs, feature_path, match_path)
