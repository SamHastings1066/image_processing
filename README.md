![Image with embedding](output/fitness_poses_images_out/star/frame_34.jpg "Image with embedding")

# Image Processor

Image Processor is a python directory containing two files that together convert `MOV` files into `csv` files. Each `MOV` file captures multiple angles of a single human body pose. Each `csv` file maps to a single `MOV` and each row in a given `csv` is the vector representation of the pose from a specific frame in the corresponding `MOV` file. These vector representations are used in a downstream KNN model that classifies human body poses from a streaming video input.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to set up the environment.

```bash
pip install -r requirements.txt
```

## Usage

### 1. Convert MOVs to jpgs

**N.B. `MOV` input files should be stored in `./input_videos`**

The `MOV` files should be video recordings of statically held poses (e.g. a left leg lunge, a squat, the up position of a pull-up, etc.). The recordings should be videos showing the pose from multiple different angle e.g. by having the cameraperson walk a full circle around the subject as the subject holds the pose (tough for some poses!).

Before image embeddings can be processed these files must first be converted into .jpg format using `process_videos.py`. This is a python file which extracts image frames from the `MOV` files into `jpg` format skipping `skip_frames` at a time.

To convert `MOV` files to `jpg`  using the default value of `skip_frames=7` run:

```bash
python process_videos.py
```
Otherwise specify the value of skip frames using:

```bash
python process_videos.py --skip_frames <num_frames>
```
The `jpg` files will be stored in subdirectories within the `input_jps` directory. Each subdirectory will take the name of the `MOV` file from which the `jpg` files it contains were generated.

### 2. Convert jpgs to vector embeddings

Simply open the `create_embeddings.ipynb` notebook and run all the cells. There are more details on how the embeddings are generated and how to customize the embedding process within the notebook, so please see the notebook for further info, but the main model being used is from Google's mediapipe suite.

`.csv` output files are automatically output to `./output/fitness_poses_csv_out` and this is the folder that should be imported into the webapp for the downstream KNN model.
