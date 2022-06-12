ece209as_project
================

Video Super-Resolution based on selected Alignment Methods with New Evaluations.
--------------------------------------------------------------------------------

### Zichao Xian, Yuanlong Chen, Boya Ouyan.

##### Group repository for UCLA ECE209AS projects.

Repository contains:

-   [Docs](docs)/ for website content

-   [Software](software)/ for code used in your project

-   [Data](data) for data data used in your project

 

Add your project's code to this folder.

To install the project there are the steps you need to do

Step 1: Create a Conda environment and activate it

conda create --name zichao python=3.8 -y

conda activate zichao

 

Step 2: Install PyTorch

On the GPU platforms:

conda install pytorch=1.10 torchvision cudatoolkit=11.3 -c pytorch

 

Step 3: Install pre-built MMCV using MIM

pip3 install openmim

mim install mmcv-full==1.5.0

 

Step 4: Install our project from the source code

git clone https://github.com/JayChen9909/ece209as_project.git

cd mmediting

pip3 install -e .

 

Step 5. Verification

cd \~

python -c "import mmedit; print(mmedit.__version__)"

\# Example output: 0.14.0

 

After the installation, you needs to prepare the dataset, we mainly use REDS4 as
our data set, you can download data
[here](https://seungjunnah.github.io/Datasets/reds.html). What you need download
is train_blur , val_blur and test_blur. And unzip it into the target folder.

The dataset needs to be set as

mmediting

├── mmedit

├── tools

├── configs

├── data

│ ├── REDS

│ │ ├── train_blur

│ │ │ ├── 000

│ │ │ ├── 001

│ │ │ ├── ...

│ │ ├── train_sharp

│ │ │ ├── 000

│ │ │ ├── 001

│ │ │ ├── ...

 

Then the basic preparation is finished. Now you need to prepare the config file.
The config file is in the .\\software\\mmediting\\mmediting\\configs\\restorers

 

for the one without alignment method the config file is

\\software\\mmediting\\mmediting\\configs\\restorers\\basicvsr\\basicvsr_reds4.py

 

for the one with optical flow alignment, the config file is

\\software\\mmediting\\mmediting\\configs\\restorers\\real_basicvsr\\realbasicvsr_wogan_c64b20_2x30x8_lr1e-4_300k_reds.py

 

 

for the one with DCN alignment, the config file is

\\software\\mmediting\\mmediting\\configs\\restorers\\basicvsr_plusplus\\basicvsr_plusplus_c64n7_8x1_600k_reds4.py

 

The config file has a lot of parameters. To run it one you computer, you need to
change some of them.

 

Step 1:

You need change the data path in train_dict

lq_folder='data/REDS/train_blur',

gt_folder='data/REDS/train_sharp',

also change the val_dict

(Sometime you can not handle such big dataset. You need delete some folders in
the train data. But the reading program will read 270 folder anyway. So you need
to change some code in
\\software\\mmediting\\mmediting\\mmedit\\datasets\\sr_reds_multiple_gt_dataset.py

in the line 58, the code is keys = [f'{i:03d}' for i in range(0, 270)]

you need to change the range(0,270) to (0,the num you want))

 

Step 2:

To train the model, you need have enough GPU memory. Or you can change some
parameter in the config file to minimize the data size. The most important
parameter is num_input_frames. I set it as 2. You can also increase the batch
size to minimize the data. The data size is workers_per_gpu.

 

Step 3:

use the command to start a train.

./tools/dist_train.sh \${CONFIG_FILE} \${GPU_NUM}

the example command is

./tools/dist_train.sh configs/restorers/basicvsr/basicvsr_reds4.py 1
