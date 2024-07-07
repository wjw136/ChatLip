<div align="center">

# Chat-Wav2lip

A comprehensive model for voice-driven lip movement generation.

</div>


## Introduction
This project ensembles two open-source project, [ChaTTS](https://github.com/2noise/ChatTTS) and [EasyWav2Lip](https://github.com/anothermartz/Easy-Wav2Lip).

## Example
<table>
<tr>
<td align="center">

**Initial Video** 

</td>
<td align="center">

**Text**

</td>
<td align="center">

**Generated Video**

</td>

</tr>
<tr>
<td align="center"  width="200" height="200">
<!-- <video controls  width="200" height="200">
  <source src="./data/example/one.mp4" type="video/mp4">
</video> -->

[![video](./data/example/one.mp4)](./data/example/one.mp4)

</td>
<td align="center" width="200" height="200">

最近天气逐渐变热了，大家有出去游玩或者做些什么特别的活动吗？我昨天去了一个新的咖啡馆，环境特别好，咖啡也很美味，推荐大家有时间可以去试试哦。


</td>
</td>
<td align="center" width="200" height="200">

<!-- <video controls  width="200" height="200">
  <source src="./data/example/one_process.mp4" type="video/mp4">
</video> -->

[![video](./data/example/one_process.mp4)](./data/example/one_process.mp4)
</td>
</tr>

<tr>
<td align="center" width="200" height="200">
<!-- <video controls  width="200" height="200">
  <source src="./data/example/two.mp4" type="video/mp4">
</video> -->

[![video](./data/example/two.mp4)](./data/example/two.mp4)

</td>
<td align="center" width="200" height="200">

水壶的盖子设计得非常人性化，采用一键开盖，使用起来非常方便。壶口设计宽大，不仅方便倒水，还容易清洗，不会留下任何死角。壶身还有防滑设计，即使手上有水也不容易滑落。

</td>
</td>
<td align="center" width="200" height="200">

<!-- <video controls  width="200" height="200">
  <source src="./data/example/two_process.mp4" type="video/mp4">
</video> -->
[![video](./data/example/two_process.mp4)](./data/example/two_process.mp4)
</td>
</tr>
</table>

## Get Started
### Environment Setup
```bash
# base setting
conda create -n chatlip
conda activate chatlip
pip install -r requirements.txt

# ffmpeg related package
ENV_BIN_DIR=$(echo $CONDA_PREFIX)/bin
curl -O https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz
tar -xf ffmpeg-release-amd64-static.tar.xz
rm ffmpeg-release-amd64-static.tar.xz
for file in ffmpeg ffprobe ffplay; do
    curl -O "https://evermeet.cx/ffmpeg/${file}-6.1.1.zip"
    unzip "${file}-6.1.1.zip"
done
mv -f ffmpeg-7.0.1-amd64-static/ffmpeg $ENV_BIN_DIR/
mv -f ffmpeg-7.0.1-amd64-static/ffprobe $ENV_BIN_DIR/
rm -rf ffmpeg-7.0.1-amd64-static
```

### Model Prepare
```bash
# ChatTTS
#* automated download when first used

# EasyWav2Lip
cd Easy-Wav2Lip/
python install.py
cd ../
```
### Quick Start
```bash
sh start.sh
```

## Future Work / Existing Problems

- [ ] Inability to process numbers into audio; frontend handling required.
- [ ] Sometimes a bit blurry on lips.
- [ ] When the video is played in a loop, it will be disconnected as if the frame is dropped.
- [ ] The pause in the audio doesn't exactly line up with the stop of the mouth movement in the video.
- [ ] There is a chance that the voice and lip movements may not match, and redundant lip movements are often observed.
- [ ] Small lips will make some mistakes on lip actions generation, sometimes even producing new lips. 
- [ ] If the sound characteristics are inconsistent with the characteristics of the characters in the scene, it is easy to feel inconsistent.
- [ ] Long text piece inputs will cause audio incomplete with undesirable truncation.
- [ ] The generation lacks real-time performance (both for audio and video).
