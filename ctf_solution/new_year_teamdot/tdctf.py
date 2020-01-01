import string
restrictions = ['qohrjzsvlxaah_dpjjwfgyobgclqtznrxdz', 'mpuvuegnkurhvuhokmvrjixtxsepgtlsovf', 'cmsxmkmkupkouowfngkhfbmhtrnci_gywgw', 'svcsdplbejibpejuzqtuvqycvzmuuhbbfsy', 'lgblcwitqkepxwkatx_a_craptrobpwvuus', 'krdzoled_dcvqacyvoyimmjssqaahitezym', 'dklwrxdigqvxfcidgbpxboeobjxensdq_fj', 'thqcpupunc_uwmbkbtqcivwwngpyxfvilnu', 'rwedvffwiwzyyvlwrpejkeki_etmwkrlhjr', 'vlmhtqrfpopgnkuhevzdwt_mhvszmruzsea', 'ybtthrqlrhnnbstzyzfsqrikibolpczhntb', 'js_mxhohcnljgtqrdunwaalyldbwcdiwakq', 'puniwshqxvgcshssqygphsguu_uravkdkzg', 'fxvebaa_tiukjjgxhisztdanqxwjkuanqxn', '__oyibuabyttzgnepfrgeptfaigfqxeaclx', 'otjjqiwcjmwliqoqwnokulhemhfgrwcmgb_', 'gjiosykjftxiopajssmyzxzjzainjg_jval', 'nyxnkgcpofq_rzelfwxepgsgflqbljskbrc', 'aiygfozxsgmftipimcimsuqdcwkioyqfiie', 'beaqnttodesdklyvueubrzpqkyzsfqxup_v', 'zffblj_gzzowdyznalb_chnzyocxylhpemd', 'uqwfzvjmabdrebfgidcnokulrfdv_mpgywp', 'ink_acxymsjz_nv__rjvdndxjpj_snyothh', 'xdga_mysvabmmxrmxhltxjbpdkhhvefxjqo', 'wzzkgnvrhrhqldxbcahoyfvvwnyddoocmpi', 'ecruedbzylfscfmclkdqnwc_euvkzbjtrck']
a = string.ascii_lowercase
alpha = set(list(a))
# print(alpha)
st = ""
for pos in range(len(restrictions[0])):
    given = []
    for i in restrictions:
        given.append(i[pos])
    req = list(alpha - set(given))
    if len(req):
        st = st + req[0]
    else:
        st = st + '_'
print(st)
