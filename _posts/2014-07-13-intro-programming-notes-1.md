---
title: '《算法竞赛入门经典》笔记1'
layout: post
tags:
    - 编程
---

## 第一部分 语言篇

### 第一章 程序设计入门

#### 1.1 printf的用法 //
例子

    #include <stdio.h>
    int main()
    {
        printf("%.1lf\n", 8.0 / 5);
    }

参考"C programming language"

    int printf(char *format, arg1, arg2, ...)

format中在字符%和**转换字符**中间可能从左到右依次包含以下组成部分

+ 负号， 左对齐形式（默认右对齐）输出
+ 数， 用于指定最小字段宽度。打印参数将不小于最小字段宽度，字段左边（如果使用左对齐，则为右边）多余的字符位置用空格填充以保证最小字段宽
+ 小数点，用于将字段宽度和精度分开
+ 数，用于指定精度，即字符串中要打印的最大字符数、浮点数小数后的位数、整型最少输出的数字数目。
+ 字母h或l，h表示将整型作为short打印，l表示将整型作为long打印

转换字符

    d,i--------------int；十进制
    o----------------int；无符号八进制（没有前导0）
    x,X--------------int；无符号16进制（没有前导0x或0X）
    u----------------int；无符号十进制
    c----------------int；单个字符
    s----------------char *；顺序打印字符串中的字符，直到遇到'\0'或已打印了由精度指定的字符为止
    f----------------double；十进制

整数和整数运算得整数，浮点数和浮点数运算得浮点数，**整数和浮点数运算先把整数变成浮点数在运算得浮点数**。


浮点数可以转成int值，但会失去小数信息。

---

#### 1.2 scanf的用法

    int scanf(char *format, ...)

scanf函数从标准输入中读取字符序列，按照format中的格式说明对字符序列进行解释，并把结果以其形式保存在参数**指针**指的相应的位置。scanf函数有返回值，就是成功读入的变量的个数。

空格、TAB和回车符是无关紧要的。

---

#### 1.3 变量值的交换
交换a、b值

经典方式:

    t = a;
    a = b;
    b = t;

技巧

    a = a + b;
    b = a - b;
    a = a - b;

**tips:重要的是解决问题，而不是一味地炫耀程序编写的技巧**

#### 1.4 if 语句
if语句的条件是个逻辑表达式，值为0或1，用短路（short-circuit）计算。

#### 1.5 溢出       // TODO(参考CSAPP)
整数溢出成符号奇怪的数。

#### 1.6 总结
1. 重视实验，哪怕不理解背后的原理也要清楚现象。要学会实验的方法，这样编程时即使忘记了一些细节也能通过实验得出结论。
2. 编程时，学会模仿。学习的时候要抓住主要矛盾。要把事情做好，就必须要学得透彻，但没有必要操之过急。

---

### 第二章 循环结构程序设计

#### 2.1 判断一个数n是否为完全平方数
    /*
    floor函数的作用是取整
    floor(m + 0.5)的作用是四舍五入
    */
    
    int n;
    double m;
    
    m = sqrt(n);
    if (floor(m + 0.5) == m)
        printf("OK");
    else
        printf("No")

之所以要这样处理是因为浮点运算存在误差

#### 2.2 小技巧
+ 通过输出中间结果来查错
+ 利用取模操作来是变量值不至于溢出
+ 利用<time.h>库函数来查看程序运行时间
  （printf("Time used = %.10f\n", (double clock() / CLOCKS_PER_SEC));）

#### 2.3 输入的数的个数不确定
输入n个数取最大值。求解问题**关键在于输入的数的个数不确定。**

    #include <stdio.h>
    #define INF 1000000
    
    int main()
    {
        int x, max = -INF;
    
        while (scanf("%d", &x) == 1) {
            if (x > max)
                max = x;
        }
    
        return 0;
    }

scanf函数有返回值，就是成功读入的变量的个数。

+ 如何告诉程序输入结束了？在Linux下，输入完毕后按Ctrl+D键即可
+ 变量在未赋值前的值是不确定的，所以要**赋初值**

#### 2.4 使用文件最简单的方法是使用输入输出重定向
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

#### 2.5 ifdef 选择编译
只有当LOCAL定义了，在#ifdef和#endif间的内容才会编译。

    #define LOCAL
    #include <stdio.h>
    int main()
    {
    #ifdef LOCAL
        freopen("data.input", "r", stdin);
        freopen("data.output", "w", stdout);
    #endif
    
        printf("Hello, world\n");
        return 0;
    }
