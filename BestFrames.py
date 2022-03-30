import os

def creat_psnr_log(source,encode)->str:
    '''
    creating PSNR log
    :param source:the source clip file address
    :param encode:the encode clip file address
    :return:content ->str
    example:creat_psnr_log(r"H:\vstest_outputs\crf\crf_16.4.mkv",r"H:\vstest_outputs\crf\crf_16.6.mkv")
    '''
    cmd = f'ffmpeg -i {source} -i {encode} -lavfi psnr="stats_file=psnr.log" -f null -'
    rlt = os.popen(cmd)
    content = rlt.read()
    return  content

def creat_ssim_log(source,encode)->str:
    '''
    creating SSIM log
    :param source: the source clip file address
    :param encode: the encode clip file address
    :return: content->str
    example:creat_ssim_log(r"H:\vstest_outputs\crf\crf_16.4.mkv",r"H:\vstest_outputs\crf\crf_16.6.mkv")
    '''
    cmd = f'ffmpeg -i {source} -i {encode} -lavfi ssim="stats_file=ssim.log" -f null -'
    rlt = os.popen(cmd)
    content = rlt.read()
    return  content

def psnr_sort(source,encode):
    '''
     Making a list of every frame's PSNR and ordered by descending order.
    :param source: the source clip file address
    :param encode: the encode clip file address
    :return:
    example:psnr_sort(r"H:\vstest_outputs\crf\crf_16.4.mkv",r"H:\vstest_outputs\crf\crf_16.6.mkv")
    '''
    creat_psnr_log(source, encode)
    psnr_log_location = 'psnr.log'
    psnr_list = []
    f = open(psnr_log_location, 'r', encoding='utf-8')
    contents = f.readlines()
    flag = 1
    sum_of_psnr = 0
    for i in contents:
        psnr_avg_index = i.find('psnr_avg:')
        try:
            psnr_avg = float(i[psnr_avg_index + 9:psnr_avg_index + 14])
        except ValueError:
            psnr_avg = 0
            psnr_turple = (flag, psnr_avg)
        else:
            psnr_turple = (flag, psnr_avg)
        psnr_list.append(psnr_turple)
        flag += 1
        sum_of_psnr += psnr_avg
    del psnr_list[0]
    # average_psnr_num = sum_of_psnr / len(psnr_turple)  # average psnr
    psnr_sorted = sorted(psnr_list, key=lambda x: x[1], reverse=True)  # sort
    print(psnr_sorted)

def ssim_sort(source,encode):
    '''
    Making a list of every frame's SSIM and ordered by descending order.
    :param source: the source clip file address
    :param encode: the encode clip file address
    :return:
    example:ssim_sort(r"H:\vstest_outputs\crf\crf_16.4.mkv",r"H:\vstest_outputs\crf\crf_16.6.mkv")
    '''
    creat_ssim_log(source, encode)
    ssim_log_location = 'ssim.log'
    ssim_list = []
    f = open(ssim_log_location, 'r', encoding='utf-8')
    contents = f.readlines()
    flag = 1
    sum_of_ssim = 0
    for i in contents:
        ssim_avg_index = i.find('All:')
        try:
            ssim_avg = float(i[ssim_avg_index + 4:ssim_avg_index + 12])
        except ValueError:
            ssim_avg = 0
            ssim_turple = (flag, ssim_avg)
        else:
            ssim_turple = (flag, ssim_avg)
        ssim_list.append(ssim_turple)
        flag += 1
        sum_of_ssim += ssim_avg
    del ssim_list[0]
    # average_ssim_num = sum_of_ssim / len(ssim_turple)  # average SSIM
    ssim_sorted = sorted(ssim_list, key=lambda x: x[1], reverse=True)  # sort
    print(ssim_sorted)


