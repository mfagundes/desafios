"""
Depois de algumas horas de estudo eu consegui achar uma função que resolveria o problema 'like a charm'

É possível que eu não consiga a vaga por não ter conseguido finalizar o desafio.

mas tenho certeza que por esse problema isso não vai acontecer mais.

Vou estudar esse reduce ^_^
"""

from functools import reduce
from time import time

def get_subsetsum(n):
    soma = 0
    # val = set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    val = {i+n//i for i in range(1, int(n**0.5) + 1) if n % i == 0}
    for v in val:
        soma += v
    return soma


def maxSubsetSum(k):
    """
    >>> maxSubsetSum([12])
    [28]

    :param k:
    :return:
    """
    result = []

    for index in range(len(k)):
        number = k[index]
        soma = get_subsetsum(number)
        result.append(soma)

    return result


valores = [386349, 636988, 563618, 950759, 477206, 398652, 159489, 832149, 727774, 483591, 652140, 779275, 82812, 636257, 817397, 921169, 789339, 807013, 597417, 93399, 167832, 11891, 412770, 441850, 526938, 37764, 839401, 355045, 735048, 50270, 743109, 598420, 249323, 986978, 804, 163956, 799010, 722435, 576997, 572711, 327740, 661265, 250304, 543267, 533494, 522611, 543187, 316282, 545616, 464948, 275913, 437940, 174798, 622836, 742953, 877976, 774216, 471039, 467769, 876874, 685358, 697786, 519500, 623886, 78428, 869625, 472495, 752170, 71446, 522414, 327212, 163178, 352224, 348605, 541881, 737597, 391421, 86315, 473089, 585725, 221058, 453940, 211468, 402828, 4181, 696635, 489357, 869978, 6663, 873308, 921864, 159746, 460172, 982173, 712862, 391700, 301907, 31556, 956534, 250414, 431558, 75138, 725578, 134083, 268384, 566221, 232203, 642557, 358565, 552779, 637554, 806335, 100867, 70250, 454948, 754563, 200131, 975628, 193985, 936227, 560172, 769632, 860490, 64115, 169972, 774988, 205292, 248075, 568995, 244678, 433773, 597986, 681095, 132802, 950066, 383253, 803854, 357958, 136939, 824264, 604611, 787289, 97435, 879971, 946920, 21337, 698183, 717118, 888748, 682028, 454843, 288919, 478089, 52495, 462131, 116736, 620796, 818762, 534765, 375318, 706914, 352772, 492681, 16683, 225196, 810802, 498009, 284229, 637887, 637419, 904779, 68928, 583723, 261528, 647344, 219726, 69, 435911, 915496, 549599, 46498, 446814, 353004, 139803, 369011, 845996, 367864, 685708, 196536, 854491, 104851, 249369, 527522, 745858, 636028, 632173, 593098, 829911, 48115, 951799, 184839, 570690, 521377, 815882, 94255, 613964, 709028, 381540, 768430, 460086, 447419, 646795, 64956, 620774, 312395, 132051, 325950, 907964, 407244, 335869, 469563, 632132, 331475, 946362, 807225, 62660, 933372, 129421, 511603, 527860, 724211, 595790, 179130, 884237, 303648, 223626, 68518, 676730, 163501, 415752, 827126, 697835, 882868, 701287, 993931, 552905, 977482, 247650, 419774, 279108, 169123, 844726, 346905, 225799, 527008, 327450, 116537, 255437, 761148, 602221, 142334, 709197, 84302, 966574, 417964, 388881, 838843, 283684, 318049, 30949, 405884, 549598, 953075, 819306, 997960, 741269, 531877, 283658, 556382, 62957, 286726, 600901, 355441, 464154, 591911, 362794, 917615, 752544, 790199, 111842, 52080, 600306, 486205, 780903, 125816, 921532, 756464, 330834, 897641, 18429, 943542, 479505, 593736, 556939, 173112, 882615, 846121, 942522, 374558, 721901, 534714, 708696, 224812, 484294, 529002, 940751, 750648, 991921, 881588, 123246, 877767, 426567, 534092, 174337, 337220, 177220, 401700, 599580, 678812, 475155, 226587, 792119, 151224, 662722, 896067, 655155, 179864, 339861, 904845, 87163, 598409, 720374, 83795, 80005, 64131, 612554, 62466, 585720, 617313, 800222, 255523, 872936, 652989, 244480, 962180, 667516, 272679, 201066, 316231, 683953, 834370, 467226, 830918, 575095, 250236, 944317, 772322, 925753, 660968, 305673, 504551, 927354, 434874, 569450, 225117, 718235, 382558, 58452, 30382, 685177, 457205, 67127, 926895, 384179, 554605, 622737, 856140, 152265, 3387, 23837, 400853, 305760, 19000, 541097, 653087, 1058, 121878, 87429, 252056, 229442, 577789, 575383, 248683, 744861, 275654, 971148, 623756, 8188, 979026, 8553, 335136, 541750, 834120, 917951, 880012, 836914, 300395, 176957, 813017, 417290, 564052, 134495, 802433, 519436, 23248, 440453, 807065, 246682, 837144, 168222, 891738, 808433, 743017, 258563, 134157, 135686, 840000, 882400, 170771, 530764, 372020, 996173, 710542, 758483, 228015, 914811, 240944, 967626, 818186, 499209, 194590, 181477, 798277, 979766, 751552, 418969, 89248, 71985, 110248, 704324, 648024, 632397, 536028, 703339, 864129, 678544, 244802, 121371, 154684, 903978, 358055, 731056, 392150, 508739, 959339, 670388, 158973, 79597, 95949, 161183, 415520, 811001, 938639, 374524, 879970, 537253, 243205, 826029, 750842, 149363, 138432, 58821, 741546, 301845, 919697, 537171, 983833, 116228, 694204, 67134, 761423, 505967, 696891, 741836, 799949, 842192, 584683, 18301, 748615, 188955, 308887, 682580, 798975, 651601, 327008, 128053, 965823, 563313, 795654, 135209, 125484, 542236, 458742]


start_time = time()
print(maxSubsetSum(valores))
print("--- %s seconds ---" % (time() - start_time))

# print(maxSubsetSum([12]))