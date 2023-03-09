"""
Extract video for doctor observe, from the raw video dataset, like /data/dataset.

There are four diseases in dataset, as a result of slicing a long video into a short one.
The doctor needs to observe the beginning and the end of a set of videos.
This program takes the beginning and end videos and saves them in 1s 10 frames as a new video for the doctor to observe.
"""

# %%
import os 
import sys 
import shutil

# there should exchange the path with yourself path.
sys.path.append('/workspace/Walk_Video_PyTorch/project')

import warnings
warnings.filterwarnings("ignore")

from argparse import ArgumentParser
from torchvision.io import read_video, read_video_timestamps, write_video
import torch

from pytorchvideo.transforms.functional import uniform_temporal_subsample

# %%

def del_folder(path, *args):
    '''
    delete the folder which path/version

    Args:
        path (str): path
        version (str): version
    '''
    if os.path.exists(os.path.join(path, *args)):
        shutil.rmtree(os.path.join(path, *args))


def make_folder(path, *args):
    '''
    make folder which path/version

    Args:
        path (str): path
        version (str): version
    '''
    if not os.path.exists(os.path.join(path, *args)):
        os.makedirs(os.path.join(path, *args))
        print("success make dir! where: %s " % os.path.join(path, *args))
    else:
        print("The target path already exists! where: %s " % os.path.join(path, *args))


# %%
def get_Diease_Path_List(data_path: str):
    '''
    get the prefix data path list, like "/workspace/data/dataset/train/ASD", len = 4

    Args:
        data_path (str): meta data path

    Returns:
        list: list of the prefix data path list, len=4
    '''

    diease_path_list = []

    for flag in ('train', 'val'):

        data_path_flag = os.path.join(data_path, flag)

        for diease_flag in (os.listdir(data_path_flag)):  # ASD, ASD_not

            data_path_diease_flag = os.path.join(data_path_flag, diease_flag)

            diease_path_list.append(data_path_diease_flag)

    return diease_path_list

# %%
def get_final_video_path_Dict(prefix_path_list: list):
    '''
    get the all final video full path, in dict. 
    the keys mean the unique data with the disease.
    the values mean in on data with disease, how many file they are, store in List.

    Args:
        prefix_path_list (list): the prefix path list, like /train/ASD; /train/ASD_not; /val/ASD; /val/ASD_not.

    Returns:
        Dict: the all final video full path, store in dict.
    '''

    final_video_path_Dict = {}

    for data_path_flag_diease in prefix_path_list:

        compare_video_name_list = []

        # all video path
        video_path_list = os.listdir(data_path_flag_diease)

        # start compare video path list
        for compare_video_name in video_path_list:

            compare_video_name_list.append(compare_video_name[:15])

        compare_video_file_name = list(set(compare_video_name_list))

        for name in compare_video_file_name:

            video_same_path_list = []

            for video_path_name in video_path_list:

                now_video_path_name = video_path_name[:15]

                if now_video_path_name in name:

                    # store the full path of unique data with diease in a list.
                    video_same_path_list.append(os.path.join(data_path_flag_diease, video_path_name))

            video_same_path_list.sort()

            final_video_path_Dict[os.path.join(data_path_flag_diease, name[:15])] = video_same_path_list

    return final_video_path_Dict

# %%
def extract_video_frame(path: str, flag: str, save_path: str, uniform_temporal_subsample_num: int):
    '''
    extract vdieo from raw clipped video.

    Args:
        path (str): video path to read one video.
        flag (str): start or end video. choice from ["start", "end"]
        save_path (str): extracted video save path.
        uniform_temporal_subsample_num (int): uniform temporal subsample number, such as unifrom extract 10 frames from 30 frames.
    '''    
    
    # bias to control the bias of start frames and end frames.
    bias = 40

    video, _, info = read_video(path)

    fps = round(info['video_fps'])
    print('current fps: %s' % fps)

    currt_name = path.split('/')[-1].split('.')[0] + '_' + flag + '.mp4'
    file_save_path = os.path.join(save_path, currt_name)
    
    if flag == 'start':
        video_tensor = video[bias:fps+bias]

        extracted_video = uniform_temporal_subsample(video_tensor, num_samples=uniform_temporal_subsample_num, temporal_dim=0)
        print(extracted_video.shape)
        write_video(filename=file_save_path, video_array=extracted_video, fps=uniform_temporal_subsample_num)
    
    else:
        video_tensor = video[-fps-bias:-bias]
        extracted_video = uniform_temporal_subsample(video_tensor, num_samples=uniform_temporal_subsample_num, temporal_dim=0)
        print(extracted_video.shape)
        write_video(filename=file_save_path, video_array=extracted_video, fps=uniform_temporal_subsample_num)

# %%

def get_parameters():

    parser = ArgumentParser()

    # Path
    parser.add_argument('--data_path', type=str, default="/workspace/data/dataset/", help='meta dataset path')
    parser.add_argument('--observe_path', type=str, default="/workspace/data/observe_dataset",
                        help="extracted video save path.")
    parser.add_argument('--uniform_temporal_subsample_num', type=int,
                        default=10, help='num frame from the clip duration')

    return parser.parse_known_args()


# %%
if __name__ == '__main__':

    # for test in jupyter
    parames, unkonwn = get_parameters()

    DATA_PATH = parames.data_path
    SAVE_PATH = parames.observe_path
    uniform_temporal_subsample_num = parames.uniform_temporal_subsample_num

    make_folder(SAVE_PATH)

    prefix_path_list = get_Diease_Path_List(DATA_PATH)  # four folder, train/ASD, train/ASD_not, val/ASD, val/ASD_not

    final_video_path_Dict = get_final_video_path_Dict(prefix_path_list)

    for key in final_video_path_Dict.keys():
            
        one_list = final_video_path_Dict[key]
        one_list.sort()

        start = one_list[0] 
        end = one_list[-1]

        print('current start path: %s' % start)
        print('current end path: %s' % end)
        
        extract_video_frame(start, 'start', SAVE_PATH, uniform_temporal_subsample_num)
        extract_video_frame(end, 'end', SAVE_PATH, uniform_temporal_subsample_num)

    print('*' * 30)
    print('finish extract video')


