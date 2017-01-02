---
title: 'Computer Network 笔记 2'
layout: post
tags:
    - 计算机网络
    - coursera
---

### Week Two

#### 2.1 Physical Layer Overview

&emsp;&emsp;物理层关心的是信息如何在链路（link）中传送。有模拟信号（analog signals）和数字信号(digital bits)。

---

1. 考虑传输介质的性质
   + wires, fiber optics, wireless
2. 信号传输要素
   + 带宽（bandwidth）, 衰减（attenuation）, 噪音（noise）
3. 调制(modulation schemes)
   + 如何表示位(bits)和噪音问题
4. 限制
   + Nyquist, 香农（Shannon）公式

---

**延迟(delay)**

+ Transmission delay: time to put M-bit message "on the wire" (M/R)
+ Propagation delay(传输延迟): time for bits to propagate across the wire(D)
+ L = M/R + D

---

**Bandwidth-Delay Product**

+ Imagine messages take space on the wire.
+ BD(bandwidth delay) = rate * delay

---

#### 2.2 Media(传输介质)

**Wires-Tristed Pair**(双绞线)

+ 在LAN和电话线中使用频繁
+ 将两根线绕在一起减小辐射和信号衰减

---

**Fiber（光纤）**

+ 带宽很大，能够长距离传输
+ 单模光纤和多模光纤（能有多个信道，但传输的距离有限）

---

**Wireless(无线)**

+ 同时向一个区域发信号，可能有多个接收者和有线不同
+ 相同频率的信号会互相干扰。

---

**多路复用**

+ FDM（Frequency Division Multiplexing, 频分多路复用）：分频率，带宽降低
+ TDM（Time Division Multiplexing, 时分多路复用）：用户随着时间片，轮流使用带宽

---

**CDMA(Code Division Multiple Access码分多路访问)**

+ 应用在移动电话通信领域，一个移动电话系统
+ 比喻：CMDA就像大厅里每个人都在讲话但每一对都使用不同的语言。
+ 每个站都被分配一个唯一的m位时间片序列代码。传输1时，就把时间片序列发出去，传输0时，就把时间片序列的补码发出去。每个站的时间片序列相互正交。 **S *  T = 0， S * S = 1**
+ 一个站接受的信息是其他站发出信息的叠加，它必须预先知道发出站的时间序列，与接受到的时间序列求**内积**就完成恢复工作。如果是发出站的时间序列，那么发送的是1，如果是发出站的时间序列的补码那发送的就是0
+ 因此，原来每秒发送b位，现在变成了每秒发送mb个位，所需的信息量变成了原来的m位，所以只有当前可用带宽是原来可以带宽的m倍时此方案才可用。

---

#### 2.3 Signals(信号)

**傅里叶变换**

+ 一个信号可能是由多个频率不同的波叠加而成
+ 当频率和带宽下降时，信号衰减

---

**信号有线传递**

+ 信号会衰减
+ 信号会延迟
+ 频率会降低
+ 噪音会出现在信号中
+ 光在三个频率带宽上传递衰减得下

---

**信号无线传递**

+ 以光速传递
+ 多个相同频率的信号会互相干扰（spatial reuse） // TODO
+ 多径衰减(WireLess multipath)，信号通过多个、不同路径（因为反射）传输 ，相位发生变化，因而抵消了信号。

---

#### 2.4 Modulation(调制)

&emsp;&emsp;调制就是信号和位的对应关系。

---

**简单的调制**

+ 高电压代表1，低电压代表0
+ It's called NRZ(Non-Return to Zero)

---

**Manchester coding（曼切斯特编码）**

+ 没有使用外部时钟
+ 发送每一位周期被分成了两个相等的间隔。发送“1”， 第一个间隔为高电压，第二个间隔为低电压；发送“0”， 第一个间隔为低电压，第二个间隔为高电压。
+ 每个发送周期都有个中间电压的变化，接受方可依次来同步
+ 缺点：eg：为了在10Mbps速率上发送数据，则每秒信号必须改变20M次。

**差分曼切斯特编码**

+ 间隔**起始处**没有相变，则表示位“1”；有相变，表示位“0”

---

**Clock Recovery 4B-5B**

+ Map every 4 data bits into 5 code bits without long runs of zeros.
+ 一长串的0和1会让接受方和发送方的很难同步到相同的位边界，因为他们的时钟速度不同。
+ 有个专门的对应规则的表格。

---

**Passband(带通，就是有线的信道) Modulation**

+ 可以通过频率、频幅、周期来调制

---

#### 2.5 Fundamental Limits

+ Bandwidth 限制传输速率
+ 信号强度和噪音强度限制能够识别多少个信号（signal level）

---

**Nyquist Limit(奈奎斯特限制)**

+ 有V个信元/离散级数（signal levels）,忽略噪音，**最大的bit rate = 2 * bandwidth * log V**

---

**香农公式**

+ 信噪比（the signal to noise ratio）， S/N
+ 分贝 = 10 * log(S/N)//以10为底
+ 信道最大速率 = bandwith * log(1+S/N) //以2为底

---

**Wired and Wireless**

+ 有线信噪比固定、带宽固定，可以固定数据传输速率
+ 无线的信噪比变化很大，因此数据传输率根据信噪比来变化

---

**数字用户线路DLS(Digital Subscriber Line)**

+ Separate bands for upstream and downstream
+ Modulation varies both amplitude and phase (called QAM)
+ 高信噪比

---

#### 2.6 Overview of the Link Layer

&emsp;&emsp;在数据链路层上，数据是帧(frame)。

![](/media/files/2014/07/13/1.bmp)

---

**Typical Implimentation of Layers**
![](/media/files/2014/07/13/2.bmp)

---

#### 2.7 Framming

**Byte Count**

+ 帧的第一位用于表示帧的长度。
+ 问题是一旦帧的第一位错了，后面所有帧的界定都会出错。
  ![](/media/files/2014/07/13/3.bmp)

---

**Byte stuffing(字节填充)**

+ 用一个特殊字符(flag)来表示帧的开始和结尾
+ 如果帧内有flag信息，则在flag前加入一个转义字符
+ 如何在帧内有转义字符信息，则需要在转义字符前再加入转义字符
  ![](/media/files/2014/07/13/4.bmp)

---

**Bit stuffing(位填充)**

+ 用连续的6个1当flag
+ 传输前，当有5个连续的1则在后面加个0
+ 接受时，如果5个1后有个0则将0去除
  ![](/media/files/2014/07/13/5.bmp)

---

**PPP over SONET**

+ PPP(Point-to-Point Protocol): 大多数家庭计算机与Internet服务提供商进行通信的协议
+ 广泛用于SONET（Synchronous Optical NETwork, 同步光网络）上的IP包的frame
  ![](/media/files/2014/07/13/6.bmp)
+ flag is 0x7E and ESC is 0x7D // TODO 这里具体的填充我没有弄明白
  ![](/media/files/2014/07/13/7.bmp)

---

#### 2.8 Error Coding Overview
![](/media/files/2014/07/13/8.bmp)

---

![](/media/files/2014/07/13/9.bmp)

---

**Hamming Distance**

+ Distance is the number of bit flips needed to change D1 to D2
+ Hamming Distance of a code is the minimum distance between any pair of codewords.

---

**Error detection**

+ 小于等于d个的错误，需要距离为d+1的编码才能把错误给检测出来
+ 小于等于d个的错误，需要距离为2d+1的编码才能把错误给恢复

---

#### 2.9 Error Detection

**Parity Bit(奇偶校验位)**

+ 在数据后面加一个奇偶校验位。
+ 奇偶校验位的选择要这样的条件满足：所有数据加起来mod2等于1或0

---

**Checksums(校验和)**

校验和是帮助检测和纠正错误的一部分数据。

**Internet Checksum**

共有16位, 只能检测1位错误
![](/media/files/2014/07/13/10.bmp)

![](/media/files/2014/07/13/11.bmp)

**Cyclic Redundancy Check(CRC, 循环冗余校验码)**

首先有个生成多项式(generator polynomial)G(x), 最高位和最低位必须是1, 帧有m位，对于多项式M(x), 帧必须比生成多项式长。
![](/media/files/2014/07/13/12.bmp)
![](/media/files/2014/07/13/13.bmp)
基本的思想是在帧的尾部追加一个效验和，使得追加之后的帧所对于的多项式能够被G(x)除尽。接受时，接受到带效验的帧，用G(x)去除它。如果有余数，就表明传输中有错。
![](/media/files/2014/07/13/14.bmp)
实际运算时，mod2减法相当于XOR异或运算。
![](/media/files/2014/07/13/15.bmp)
+ CRC 在Ethernet, 802.11(wifi), ADSL, Cable 中广泛应用。
+ Checksum 在 Internet 中广泛应用。

---

#### 2.10 Error Correction

**Hamming Code**

要纠错d个错误，则编码的海明距离要大于等于2d+1

![](/media/files/2014/07/13/16.bmp)
编号为2的幂次方的位（1,2,4,8, ..）为效验位，剩下的位用m个数据位填充。每个效验位都使一组值的奇偶位为偶数（或奇数）, 11 = 1 + 2 + 8, 29 = 1 + 4 + 8 + 16
![](/media/files/2014/07/13/17.bmp)
接受时，重新计算每个效验位，将错误的效验位按2的幂次方从从高到低，从左到右拼起来，得到一个数，这个数上的数据发生了错误
![](/media/files/2014/07/13/18.bmp)

![](/media/files/2014/07/13/19.bmp)

![](/media/files/2014/07/13/20.bmp)

---

**LDPC**

+ Error correction 在物理层上用得很多m
+ LDPC is the future
+ Error detection(retransmission) is used in the link layer and above for residual errors
+ Correction also used in the application layer
