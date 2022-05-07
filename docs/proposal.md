# Project Proposal

## 1. Motivation & Objective

With the growing number of research about improving the quality of video and the development of neural networking applications for generating similar features within the same class, we find that it is possible to further improve the super-resolution applied to the video by revising and adding contents into the current neural network models. 

## 2. State of the Art & Its Limitations

Deep convolutional neural networks have shown promising efficiency and effectiveness in various video restoration tasks, such as video frame interpolation (VFI), video super-resolution (VSR), and video deblurring. To design an STVSR network, one straightforward way is by directly combining a video frame interpolation method (e.g. SepConv, ToFlow, DAIN etc.) and a video super-resolution method (e.g., DUF, RBPN, EDVR etc.) in a two-stage manner. It firstly interpolates missing intermediate LR video frames with VFI and then reconstructs all HR frames with VSR. However, temporal interpolation and spatial super-resolution in STVSR are intra-related. The two-stage methods splitting them into two individual procedures cannot make full use of this natural property. In addition, to predict high-quality video frames, both state-of-the-art VFI and VSR networks require a big frame reconstruction network. Therefore, the composed two-stage STVSR model will contain many parameters and is computationally expensive. [1]

## 3. Novelty & Rationale

By using both combining VFI + VSR and LSTM (long short-term memory), we want to try to add more techniques such as the spatial alignment technique, and check if it can further improve the performance of super-resolution. 

## 4. Potential Impact

If the project is successful, what difference will it make, both technically and broadly?
Basically, we expect that the revised system would perform with a higher quality of results, which may check from the improvement of PSNR and other standard values. Additionally, it is the best if we could achieve more release on the workload of the system.

## 5. Challenges

What are the challenges and risks?
Since traditionally the results of pictures at each frame after doing super-resolution are evaluated by the value of Peak Signal to Noise Ratio (PSNR), the change may be not obvious because the current research has improved the accuracy a lot. It might not be the only choice to check the improvements of the quality of results. So, it is the best if we could find other parameters to better check the performance of using different revisions to the models.

## 6. Requirements for Success

What skills and resources are necessary to perform the project?
(1)	Video preprocessing and augmentation
(2)	Combinational video frame interpolation (VFI) and video super-resolution (VSR)
(3)	Long short-term memory (LSTM) and Convolutional neural network (CNN)
(4)	Spatial alignment
(5)	Peak Signal to Noise Rate (PSNR)

## 7. Metrics of Success

Basically, we would follow to use Peak Signal to Noise Rate (PSNR) as the evaluative metric. After we explore more during the process, we will try other standards if we find they are more effective to evaluate the performance, which are such as Structural Similarity (SSIM) and Mean Structural Similarity (MSSIM).

## 8. Execution Plan

Describe the key tasks in executing your project, and in case of team project describe how will you partition the tasks.
(1)	Yuanlong Chen: Video preprocessing and augmentation, notes taking and reports writings.
(2)	Boya Ouyang: VFI + VSI combining achieve, revision of LSTM model.
(3)	Zichao Xian: Add LSTM layers in model, evaluate different spatial alignment techniques, and add into model and evaluate results.

## 9. Related Work

### 9.a. Papers

List the key papers that you have identified relating to your project idea, and describe how they related to your project. Provide references (with full citation in the References section below).

(1) Papers related to VSI and VFI:
· Dual-Stream Fusion Network for Spatiotemporal Video Super-Resolution [2]
· Learning for Unconstrained Space-Time Video Super-Resolution [3]
· Temporal Modulation Network for Controllable Space-Time Video Super-Resolution [4]
· NTIRE 2021 Challenge on Video Super-Resolution [5]
· Efficient Space-time Video Super Resolution using Low-Resolution Flow and Mask Upsampling [6]
· Space-time super-resolution with motion-perceptive deformable alignment [7]
· STSRNet: Deep Joint Space-Time Super-Resolution for Vector Field Visualization [8]
· MEGAN: Memory Enhanced Graph Attention Network for Space-Time Video Super-Resolution [9]
· FISR: Deep Joint Frame Interpolation and Super-Resolution with a Multi-Scale Temporal Loss [10]
· Space-Time-Aware Multi-Resolution Video Enhancement [11]
· Zooming Slow-Mo: Fast and Accurate One-Stage Space-Time Video Super-Resolution [12]
· Deep Space-Time Video Upsampling Networks [13]
· Space-Time Video Super-Resolution Using Temporal Profiles [14]

(2) Papers related to spatial alignment:
· Realtime video super-resolution with spatio-temporal networks and motion compensation. [15]
· Detail-revealing deep video super-resolution. [16]
· Video enhancement with task-oriented flow. [17]
· Frame-recurrent video super-resolution. [18]
· Deep video super-resolution network using dynamic upsampling filters without explicit motion compensation. [19]
· Recurrent back-projection network for video superresolution. [20]
· EDVR: Video restoration with enhanced deformable convolutional networks. [21]
· MuCAN: Multi-correspondence aggregation network for video super-resolution. [22]
· Progressive fusion video super-resolution network via exploiting non-local spatio-temporal correlations. [23]
· Efficient video super-resolution through recurrent latent space propagation. [24]
· Video super-resolution with temporal group attention. [25]
· Video super-resolution with recurrent structure-detail network. [26]
· Revisiting temporal modeling for video super-resolution. [27]

### 9.b. Datasets

List datasets that you have identified and plan to use. Provide references (with full citation in the References section below).

For training:
REDS [28], Vimeo-90K [29]

For testing:
REDS4 [28], Vid4 [30], UDM10 [31], Vimeo-90K-T [29]

For validation:
REDSval4 [28]

### 9.c. Software

List software that you have identified and plan to use. Provide references (with full citation in the References section below).

## 10. References

List references corresponding to citations in your text above. For papers please include full citation and URL. For datasets and software include name and URL.

[1] Zooming Slow-Mo: Fast and Accurate One-Stage Space-Time Video Super-Resolution
Xiaoyu Xiang, Tapeng Tian, Yulun Zhang, Yun Fu, Jan P. Allebach, Chenliang Xu  
Paper: https://arxiv.org/pdf/2002.11616.pdf  
Code: https://github.com/Mukosame/Zooming-Slow-Mo-CVPR-2020

[2] Dual-Stream Fusion Network for Spatiotemporal Video Super-Resolution
Min-Yuan Tseng, Yen-Chung Chen, Yi-Lun Lee, Wei-Sheng Lai, Yi-Hsuan Tsai, Wei-Chen Chiu  
Paper: https://openaccess.thecvf.com/content/WACV2021/papers/Tseng_Dual-Stream_Fusion_Network_for_Spatiotemporal_Video_Super-Resolution_WACV_2021_paper.pdf  
Code: https://github.com/TMYuan/Dual-Stream-Fusion-Network

[3] Learning for Unconstrained Space-Time Video Super-Resolution
Zhihao Shi, Chengqi Li, Linhui Dai, Xiaohong Liu, Jun Chen, Timothy N. Davidson
Paper: https://arxiv.org/pdf/2102.13011.pdf

[4] Temporal Modulation Network for Controllable Space-Time Video Super-Resolution
Gang Xu, Jun Xu, Zhen Li, Liang Wang, Xing Sun, Ming-Ming Cheng  
Paper: https://arxiv.org/pdf/2104.10642.pdf  
Code: https://github.com/CS-GangXu/TMNet
 
[5] NTIRE 2021 Challenge on Video Super-Resolution
Sanghyun Son, Suyoung Lee, Seungjun Nah, Radu Timofte, Kyoung Mu Lee  
Paper: https://arxiv.org/pdf/2104.14852.pdf  

[6] Efficient Space-time Video Super Resolution using Low-Resolution Flow and Mask Upsampling
Saikat Dutta, Nisarg A. Shah, Anurag Mittal  
Paper: https://arxiv.org/pdf/2104.05778.pdf  
Code: https://github.com/saikatdutta/FMU_STSR

[7] Space-time super-resolution with motion-perceptive deformable alignment
Zhuojun Cai, Xiang Tian, Ze Chen, Yaowu Chen  
Paper: https://www.spiedigitallibrary.org/journals/journal-of-electronic-imaging/volume-30/issue-3/033020/Space-time-super-resolution-with-motion-perceptive-deformable-alignment/10.1117/1.JEI.30.3.033020.short?SSO=1

[8] STSRNet: Deep Joint Space-Time Super-Resolution for Vector Field Visualization
Yifei An, Han-Wei Shen, Guihua Shan, Guan Li, Jun Liu  
Paper: https://ieeexplore.ieee.org/abstract/document/9488227

[9] MEGAN: Memory Enhanced Graph Attention Network for Space-Time Video Super-Resolution
Chenyu You, Lianyi Han, Aosong Feng, Ruihan Zhao, Hui Tang, Wei Fan  
Paper: https://arxiv.org/pdf/2110.15327.pdf

[10] FISR: Deep Joint Frame Interpolation and Super-Resolution with a Multi-Scale Temporal Loss
Soo Ye Kim, Jihyong Oh, Munchurl Kim  
Paper: https://ojs.aaai.org/index.php/AAAI/article/view/6788  
Code: https://github.com/JihyongOh/FISR

[11] Space-Time-Aware Multi-Resolution Video Enhancement
Muhammad Haris, Greg Shakhnarovich, Norimichi Ukita  
Paper: https://alterzero.github.io/projects/star_cvpr2020.pdf  
Code: https://github.com/alterzero/STARnet

[12] Zooming Slow-Mo: Fast and Accurate One-Stage Space-Time Video Super-Resolution
Xiaoyu Xiang, Yapeng Tian, Yulun Zhang, Yun Fu, Jan P. Allebach+, Chenliang Xu  
Paper: https://arxiv.org/pdf/2002.11616.pdf  
Code: https://github.com/Mukosame/Zooming-Slow-Mo-CVPR-2020

[13] Deep Space-Time Video Upsampling Networks
Jaeyeon Kang, Younghyun Jo, Seoung Wug Oh, Peter Vajda, Seon Joo Kim  
Paper: https://arxiv.org/pdf/2004.02432.pdf  
Code: https://github.com/JaeYeonKang/STVUN-Pytorch

[14] Space-Time Video Super-Resolution Using Temporal Profiles
Zeyu Xiao, Zhiwei Xiong , Xueyang Fu, Dong Liu, Zhengjun Zha  
Paper: https://xueyangfu.github.io/paper/2020/MM.pdf

[15] Realtime video super-resolution with spatio-temporal networks and motion-compensation.
Jose Caballero, Christian Ledig, Aitken Andrew, Acosta Alejandro, Johannes Totz, Zehan Wang, and Wenzhe Shi  
Paper: https://openaccess.thecvf.com/content_cvpr_2017/papers/Caballero_Real-Time_Video_Super-Resolution_CVPR_2017_paper.pdf

[16] Detail-revealing deep video super-resolution. 
Xin Tao, Hongyun Gao, Renjie Liao, Jue Wang, and Jiaya Jia  
Paper: https://openaccess.thecvf.com/content_ICCV_2017/papers/Tao_Detail-Revealing_Deep_Video_ICCV_2017_paper.pdf

[17] Video enhancement with task-oriented flow.
Tianfan Xue, Baian Chen, Jiajun Wu, Donglai Wei, and William T Freeman  
Paper: https://arxiv.org/pdf/1711.09078.pdf

[18] Frame-recurrent video super-resolution. 
Mehdi S M Sajjadi, Raviteja Vemulapalli, and Matthew Brown  
Paper: https://openaccess.thecvf.com/content_cvpr_2018/papers/Sajjadi_Frame-Recurrent_Video_Super-Resolution_CVPR_2018_paper.pdf

[19] Deep video super-resolution network using dynamic upsampling filters without explicit motion compensation.
Younghyun Jo, Seoung Wug Oh, Jaeyeon Kang, and Seon Joo Kim  
Paper: https://openaccess.thecvf.com/content_cvpr_2018/papers/Jo_Deep_Video_Super-Resolution_CVPR_2018_paper.pdf

[20] Recurrent back-projection network for video superresolution.
Muhammad Haris, Greg Shakhnarovich, and Norimichi Ukita  
Paper: https://openaccess.thecvf.com/content_CVPR_2019/papers/Haris_Recurrent_Back-Projection_Network_for_Video_Super-Resolution_CVPR_2019_paper.pdf

[21] EDVR: Video restoration with enhanced deformable convolutional networks.
Xintao Wang, Kelvin C.K. Chan, Ke Yu, Chao Dong, and Chen Change Loy  
Paper: https://openaccess.thecvf.com/content_CVPRW_2019/papers/NTIRE/Wang_EDVR_Video_Restoration_With_Enhanced_Deformable_Convolutional_Networks_CVPRW_2019_paper.pdf

[22] MuCAN: Multi-correspondence aggregation network for video super-resolution. 
Wenbo Li, Xin Tao, Taian Guo, Lu Qi, Jiangbo Lu, and Jiaya Jia  
Paper: 
Code: 

[23] Progressive fusion video super-resolution network via exploiting non-local spatio-temporal correlations.
Peng Yi, Zhongyuan Wang, Kui Jiang, Junjun Jiang, and Jiayi Ma  
Paper: https://openaccess.thecvf.com/content_ICCV_2019/papers/Yi_Progressive_Fusion_Video_Super-Resolution_Network_via_Exploiting_Non-Local_Spatio-Temporal_Correlations_ICCV_2019_paper.pdf

[24] Efficient video super-resolution through recurrent latent space propagation.
Dario Fuoli, Shuhang Gu, and Radu Timofte  
Paper: https://ieeexplore.ieee.org/document/9022159

[25] Video super-resolution with temporal group attention.
Takashi Isobe, Songjiang Li, Xu Jia, Shanxin Yuan, Gregory Slabaugh, Chunjing Xu, Ya-Li Li, Shengjin Wang, and Qi Tian  
Paper: https://openaccess.thecvf.com/content_CVPR_2020/papers/Isobe_Video_Super-Resolution_With_Temporal_Group_Attention_CVPR_2020_paper.pdf

[26] Video super-resolution with recurrent structure-detail network.
Takashi Isobe, Xu Jia, Shuhang Gu, Songjiang Li, Shengjin Wang, and Qi Tian  
Paper: https://arxiv.org/pdf/2008.00455.pdf

[27] Revisiting temporal modeling for video super-resolution. 
Takashi Isobe, Fang Zhu, and Shengjin Wang  
Paper: https://arxiv.org/pdf/2008.05765.pdf

[28] Seungjun Nah, Sungyong Baik, Seokil Hong, Gyeongsik Moon, Sanghyun Son, Radu Timofte, and Kyoung Mu Lee. NTIRE 2019 challenge on video deblurring and superresolution: Dataset and study. In CVPRW, 2019. 6, 7, 10, 11

[29] Tianfan Xue, Baian Chen, Jiajun Wu, Donglai Wei, and William T Freeman. Video enhancement with task-oriented flow. IJCV, 2019. 2, 4, 5, 6, 7, 10, 12

[30] Ce Liu and Deqing Sun. On bayesian adaptive video super resolution. TPAMI, 2014. 2, 6, 7, 10, 13

[31] Peng Yi, Zhongyuan Wang, Kui Jiang, Junjun Jiang, and Jiayi Ma. Progressive fusion video super-resolution network via exploiting non-local spatio-temporal correlations. In ICCV, 2019. 1, 2, 6, 7, 10, 13

