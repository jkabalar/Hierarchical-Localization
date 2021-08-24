from pathlib import Path

#from ...utils.read_write_model import Image, write_model, Camera
from ... import localize_sfm, match_features, extract_features

dataset = Path('datasets/RIO10')
export_dir= Path('outputs/sfm/')
sfm_pairs = export_dir / 'pairs-exhaustive.txt'  # exhaustive matching
sfm_dir = export_dir / 'sfm_superpoint+superglue'
feature_conf = extract_features.confs['superpoint_inloc']
matcher_conf = match_features.confs['superglue']
feature_path = Path(export_dir, conf['output']+'.h5')
features = feature_conf['output']
match_path = Path(export_dir, f'{features}_{matcher_conf["output"]}_{sfm_pairs.stem}.h5')
results_path = outputs / 'RIO10SFM_hloc_superpoint+superglue_netvlad40.txt'  # the result file

#fx, fy, cx, cy = 756.026,756.832,270.419,492.889 # hardcoded for seq 03 01
#width, height = 960, 540
#model_name = 'PINHOLE'
#params = [float(i) for i in [fx, fy, cx, cy]]
#cam0 = Camera(
#    id=id_, model=model_name,
#    width=int(width), height=int(height), params=params)

  
#def generate_query_lists(timestamps, seq_dir, out_path):
#    """Create a list of query images with intrinsics from timestamps."""
#    intrinsics = [cam0.model, cam0.width, cam0.height] + cam0.params
#    intrinsics = [str(p) for p in intrinsics]
#    data = map(lambda ts: ' '.join([f'cam0/{ts}.png']+intrinsics), timestamps)
#    with open(out_path, 'w') as f:
#        f.write('\n'.join(data))

query_list = export_dir / 'RIO10_queries_with_intrinsics.txt'
localize_sfm.main(
    sfm_dir, query_list, sfm_pairs, feature_path, match_path, results_path)
