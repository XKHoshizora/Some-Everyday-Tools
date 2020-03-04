# 加热时间转换器

def heat_upTime(P1, P2, t1):
    '''
    将微波炉在某初始功率下的加热时间，
    转化为转化后功率下加热所需时间，
    并打印结果（单位：分钟）
    :param P1: 初始功率（单位：W）
    :param P2: 转化后功率（单位：W）
    :param t1: 初始功率下所需时间（单位：分钟）
    :return: 无
    '''
    W = P1 * (t1 * 60)
    t2 = (W / P2) / 60
    print('{0}W功率下需加热{1}分钟'.format(P2, t2))
    return None

def main():
    P1 = int(input('初始功率：'))
    P2 = int(input('转化为功率：'))
    t1 = int(input('初始功率下的加热时间：'))
    heat_upTime(P1, P2, t1)

if __name__ == '__main__':
    main()