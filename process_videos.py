import os
import cv2
import argparse

def process_videos(skip_frames):
  os.makedirs("input_jpgs", exist_ok=True)

  # For each video in the folder
  for filename in os.listdir("input_videos"):
    if filename.endswith(".MOV"):
      vidcap = cv2.VideoCapture(os.path.join("input_videos", filename))

      # Create a new folder with the same name as the video (without the extension)
      output_folder = os.path.join("input_jpgs", filename[:-4])
      os.makedirs(output_folder, exist_ok=True)

      frame_count = 0
      saved_frame_count = 0

      # Save all of its individual frames in jpg format
      while True:
        success, image = vidcap.read()
        if not success:
          break
        if frame_count % (skip_frames + 1) == 0:
          cv2.imwrite(os.path.join(output_folder, f"frame_{saved_frame_count}.jpg"), image)
          saved_frame_count += 1
        frame_count += 1

      print(f"Processed {filename}. Saved {saved_frame_count} frames.")

def main():
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description="Process videos and extract frames.")
    parser.add_argument("-s", "--skip_frames", type=int, default=7, help="Number of frames to skip between saved frames.")
    args = parser.parse_args()

    # Call the function with the specified or default skip_frames value
    process_videos(skip_frames=args.skip_frames)

if __name__ == "__main__":
    main()
