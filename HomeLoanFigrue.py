#当前程序按照以下参数进行计算
#贷款总额：1000000、还款年限：30、房贷利率：5.145%、月供：5457.18

#房贷总款
dLoanMoney = 1000000.00
#还款年限
nYear = 30
#月供
dMonthLoanMoney = 5457.18
#房贷还款总金额
dReturnMoney = dMonthLoanMoney * nYear * 12
#本金
dMoney = dLoanMoney
#折合理财收益率
dGainRate = 0.00

print("计算中，请稍后……\n")

#穷举算收益率
dGainRate = 0.05
while (1):
    dMoney = dLoanMoney
    dGainRate = dGainRate + 0.001
    for i in range(0,nYear):
        #减掉当年月供
        dMoney = dMoney - (dMonthLoanMoney * 12)
        #增加当年收益
        dMoney = dMoney + (dMoney * dGainRate)
        i = i + 1

    if dMoney > 0:
        break

print("计算结果如下：\n");

dMoney = dLoanMoney
for i in range(0,nYear):

    #减掉当年月供
    dMoney = dMoney - (dMonthLoanMoney * 12)
    #增加当年收益
    dMoney = dMoney + (dMoney * dGainRate)
    print("第" + str(i) + "年 >> " + "本金：" + str(dMoney))

dMoney = dMoney + (dMoney * dGainRate)

print("")
print("房贷总款:" + str(dLoanMoney))
print("还款年限:" + str(nYear))
print("月供:" + str(dMonthLoanMoney))
print("房贷还款总金额:" + str(dReturnMoney))
print("本金剩余金额:" + str(dMoney))
print("折合理财收益率:" + str(dGainRate))
print()