My solutions in Python to selected leetcode problems.

## Youtube

https://www.youtube.com/playlist?list=PLUyMcNNS9KiZoqPIX1uAWdoXD_rZ_mR00

#### Trim From Start

`ffmpeg -i input.mov -ss 0.8 -vcodec copy -acodec copy output.mov`

#### Enhance Audio

- Sesin düşük ve yüksek frekanslarını filtrele
- Sesin gücünü artır
- Videoya dokunma

`ffmpeg -i input.mov -filter_complex "[0:a]highpass=f=200,lowpass=f=3000,acompressor,anlmdn,volume=3.0" -c:v copy -c:a aac -b:a 192k output.mov`
