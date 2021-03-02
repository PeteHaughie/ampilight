# this just grabs the image from the webcam (or capture card) and stores it 10 times a second
ffmpeg -y -f avfoundation -video_size 720x480 -framerate 10 -i 1 -update 1 -r 1 output.jpg
