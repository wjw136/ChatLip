
export WD=$(pwd)

# audio generator
export WAV_OUTPUT_DIR="$WD/data/output"
echo "wav output dir: $WAV_OUTPUT_DIR"
cd ChatTTS/
python examples/cmd/run.py \
    "包容是对的，但是有些事情也不能总是妥协啊。比如说昨天我下班回家，想看个球赛，结果她非要看电视剧。可是那个电视剧我真的是看不下去啊，讲的都是些狗血剧情！"
cd ../

# lip generator
cd Easy-Wav2Lip/
python run.py \
    -video_file "$WD/data/input/example.mp4" \
    -vocal_file "$WD/data/output/output_audio_0.mp3" \
    -output_dir "$WD/data/output"
cd ..
