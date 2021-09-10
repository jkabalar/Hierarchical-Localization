from pathlib import Path
import argparse
from ...utils.read_write_model import Image, write_model, Camera

def generate_query_list(dataset_dir, path):
    cameras = {}
    fx, fy, cx, cy = 756.026,756.832,270.419,492.889 # hardcoded for seq 03 01
    width, height = 960, 540
    model_name = 'PINHOLE'
    params = [float(i) for i in [fx, fy, cx, cy]]
    cam0 = Camera(id=0, model=model_name, width=int(width), height=int(height), params=params)
    #intrinsics = [cam0.model, cam0.width, cam0.height] + cam0.params
    #intrinsics = [str(p) for p in intrinsics]

    queries = dataset / f'{slice_}/test-images-{slice_}.txt'
    with open(queries, 'r') as f:
        queries = [q.rstrip('\n') for q in f.readlines()]
    #RIO10/scene03/mapping/sensors/records_data/seq03_01
    #dataset_dir = "RIO10/scene03/validation/sensors/records_data/seq03_02/"
    #frame-006270.color.jpg
    #data = map(lambda ts: ' '.join([f'frame/{ts}.png']+intrinsics), timestamps)
    data = []
    for frame_id in range(1000):
        frame_id.zfill(6)
        name = dataset_dir+ "frame-"+ str(frame_id)+".color.jpg"
        intrinsics = [name, [cam0.model, cam0.width, cam0.height] + cam0.params]
        intrinsics = [str(p) for p in intrinsics]
        data.append(' '.join(map(str, p)))
    with open(path, 'w') as f:
           f.write('\n'.join(data))
