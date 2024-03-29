# Multiple File Sound eXchange
![Python](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white) ![Python Version](https://img.shields.io/static/v1?label=Version&message=3.11&style=for-the-badge&labelColor=4B8BBE&color=FFE873&logo=python&logoColor=ffffff) ![LICENSE](https://img.shields.io/static/v1?label=LICENSE&message=MIT&style=for-the-badge) [<img alt="downloadbtn" src="https://dabuttonfactory.com/button.png?t=Download&f=Ubuntu-Bold&ts=30&tc=fff&hp=15&vp=15&c=6&bgt=unicolored&bgc=238636&bs=4&bc=37914a" width="77px">](https://github.com/sanalzio/MultipleSoX/releases)

- [Multiple File Sound eXchange](#multiple-file-sound-exchange)
  - [Istallation](#istallation)
  - [Usage](#usage)
    - [Method 1](#method-1)
    - [Method 2](#method-2)
    - [Method 3](#method-3)
  - [Configuration](#configuration)
  - [SoX](#sox)
  - [License](#license)

## Istallation
[<img alt="downloadbtn" src="https://dabuttonfactory.com/button.png?t=Download&f=Ubuntu-Bold&ts=30&tc=fff&hp=15&vp=15&c=6&bgt=unicolored&bgc=238636&bs=4&bc=37914a" width="100px">](https://github.com/sanalzio/MultipleSoX/releases)

Download MutlipleSoX latest relase from [here](https://github.com/sanalzio/MultipleSoX/releases).

## Usage

### Method 1
1) Run the multipleSoX.exe file.
2) Select directory.

### Method 2
1) Drag and drop a folder into "multipleSoX.exe".

### Method 3
1) Open cmd or power shell and enter a command like this and run it
   ```powershell
   "path/to/multipleSoX.exe" "path/to/directory"
   ```

## Configuration
Open the "config.json" file with a text editor and edit it to your liking
```json
{
    "sox-dir":"",
    // SoX (Sound eXchange) direction (use empty for local sox).
    "start-path":"/",
    // DirectoryDialog start path.
    "include-subfolders":true,
    // Include files in subfolders.
    "input-types":["wav","mp3","ogg"],
    // File input types.
    "output-type":"wav",
    // Extension of the output file (use empty to be the extension of the input file)
    "default-type":"wav",
    // To use format options other than "additional-format-options", prefix them with "default-" (Equivalent to option "--type wav").
    "additional-global-options":"",
    // Additional SoX global options
    "additional-format-options":"--rate 22050 --channels 1"
    // Additional SoX format options
}
```

## SoX

```
Usage summary: [gopts] [[fopts] infile]... [fopts] outfile [effect [effopt]]...

SPECIAL FILENAMES (infile, outfile):
-                        Pipe/redirect input/output (stdin/stdout); may need -t
-d, --default-device     Use the default audio device (where available)
-n, --null               Use the `null' file handler; e.g. with synth effect
-p, --sox-pipe           Alias for `-t sox -'

SPECIAL FILENAMES (infile only):
"|program [options] ..." Pipe input from external program (where supported)
http://server/file       Use the given URL as input file (where supported)

GLOBAL OPTIONS (gopts) (can be specified at any point before the first effect):
--buffer BYTES           Set the size of all processing buffers (default 8192)
--clobber                Don't prompt to overwrite output file (default)
--combine concatenate    Concatenate all input files (default for sox, rec)
--combine sequence       Sequence all input files (default for play)
-D, --no-dither          Don't dither automatically
--dft-min NUM            Minimum size (log2) for DFT processing (default 10)
--effects-file FILENAME  File containing effects and options
-G, --guard              Use temporary files to guard against clipping
-h, --help               Display version number and usage information
--help-effect NAME       Show usage of effect NAME, or NAME=all for all
--help-format NAME       Show info on format NAME, or NAME=all for all
--i, --info              Behave as soxi(1)
--input-buffer BYTES     Override the input buffer size (default: as --buffer)
--no-clobber             Prompt to overwrite output file
-m, --combine mix        Mix multiple input files (instead of concatenating)
--combine mix-power      Mix to equal power (instead of concatenating)
-M, --combine merge      Merge multiple input files (instead of concatenating)
--multi-threaded         Enable parallel effects channels processing
--norm                   Guard (see --guard) & normalise
--play-rate-arg ARG      Default `rate' argument for auto-resample with `play'
--plot gnuplot|octave    Generate script to plot response of filter effect
-q, --no-show-progress   Run in quiet mode; opposite of -S
--replay-gain track|album|off  Default: off (sox, rec), track (play)
-R                       Use default random numbers (same on each run of SoX)
-S, --show-progress      Display progress while processing audio data
--single-threaded        Disable parallel effects channels processing
--temp DIRECTORY         Specify the directory to use for temporary files
-T, --combine multiply   Multiply samples of corresponding channels from all
                         input files (instead of concatenating)
--version                Display version number of SoX and exit
-V[LEVEL]                Increment or set verbosity level (default 2); levels:
                           1: failure messages
                           2: warnings
                           3: details of processing
                           4-6: increasing levels of debug messages
FORMAT OPTIONS (fopts):
Input file format options need only be supplied for files that are headerless.
Output files will have the same format as the input file where possible and not
overridden by any of various means including providing output format options.

-v|--volume FACTOR       Input file volume adjustment factor (real number)
--ignore-length          Ignore input file length given in header; read to EOF
-t|--type FILETYPE       File type of audio
-e|--encoding ENCODING   Set encoding (ENCODING may be one of signed-integer,
                         unsigned-integer, floating-point, mu-law, a-law,
                         ima-adpcm, ms-adpcm, gsm-full-rate)
-b|--bits BITS           Encoded sample size in bits
-N|--reverse-nibbles     Encoded nibble-order
-X|--reverse-bits        Encoded bit-order
--endian little|big|swap Encoded byte-order; swap means opposite to default
-L/-B/-x                 Short options for the above
-c|--channels CHANNELS   Number of channels of audio data; e.g. 2 = stereo
-r|--rate RATE           Sample rate of audio
-C|--compression FACTOR  Compression factor for output format
--add-comment TEXT       Append output file comment
--comment TEXT           Specify comment text for the output file
--comment-file FILENAME  File containing comment text for the output file
--no-glob                Don't `glob' wildcard match the following filename

AUDIO FILE FORMATS: 8svx aif aifc aiff aiffc al amb amr-nb amr-wb anb au avr awb cdda cdr cvs cvsd cvu dat dvms f32 f4 f64 f8 flac fssd gsm gsrt hcom htk ima ircam la lpc lpc10 lu maud mp2 mp3 nist ogg prc raw s1 s16 s2 s24 s3 s32 s4 s8 sb sf sl sln smp snd sndr sndt sou sox sph sw txw u1 u16 u2 u24 u3 u32 u4 u8 ub ul uw vms voc vorbis vox wav wavpcm wv wve xa
PLAYLIST FORMATS: m3u pls
AUDIO DEVICE DRIVERS: waveaudio

EFFECTS: allpass band bandpass bandreject bass bend biquad chorus channels compand contrast dcshift deemph delay dither divide+ downsample earwax echo echos equalizer fade fir firfit+ flanger gain highpass hilbert input# ladspa loudness lowpass mcompand noiseprof noisered norm oops output# overdrive pad phaser pitch rate remix repeat reverb reverse riaa silence sinc spectrogram speed splice stat stats stretch swap synth tempo treble tremolo trim upsample vad vol
  * Deprecated effect    + Experimental effect    # LibSoX-only effect
EFFECT OPTIONS (effopts): effect dependent; see --help-effect
```

## License
MIT