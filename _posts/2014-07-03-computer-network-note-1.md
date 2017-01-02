---
title: 'Computer Network 笔记 1'
layout: post
tags:
    - 计算机网络
    - coursera
---

---

### Week One

---

### 1.1 Goals and Motivation

The Main Point

    1. To learn how the Internet works
    2. To learn the fundamentals of computer networks

The development of Internet
![](/media/files/2014/07/03/1.bmp)
![](/media/files/2014/07/03/2.bmp)

---

Internet--Societal Impact

    An engine of economic growth
    - Advertising-sponsored search
    - "Long tail" online stores
    - Online marketplaces
    - Crowdsourcing(众筹)

---

The reason to learn the fundamentals is that all we learn could apply to all computer networks.

---

Key problem
![](/media/files/2014/07/03/3.bmp)

---

Example of upheavals in the past 1-2 decades
![](/media/files/2014/07/03/4.bmp)

### 1.2 Uses of Networks
Example Uses of Networks

    - Work
    - Home
    - Mobile

---

For User Communication

    - VoIP(voice-over-IP)
    - Video conferencing
    - Instant messaging
    - Social networking

---

For Resource Sharing

    - Many user may access the same underlying resource
    - More cost effective than dedicated resources per user.
    
    Statistical Multiplexing
    
    + Sharing of network bandwidth between users according to the statistics of their demand
      - Multiplexing just means sharing
      - Useful because users are mostly idle and their traffic is bursty.

---

Content Delivery

- Same content is deliverd to many users(web pages)
- Use **replicas** in the network

![](/media/files/2014/07/03/5.bmp)
![](/media/files/2014/07/03/6.bmp)

---

**Metcalfe's Law**

    + The value of a network of N nodes is proportional to N^2.
---

### 1.3 Network Components
Parts of a Network
![](/media/files/2014/07/03/7.bmp)
&emsp;&emsp;host是可以挂app的node，router是单纯转发信息的node.

---

Components Names
![](/media/files/2014/07/03/8.bmp)

---

Types of Links

    + Full-duplex(全双工)
      可以两边同时传信息
    + Half-duplex(半双工)
      两边都可以传信息，但不能同时传
    + Simplex(单工)
      只有一边能传信息

---

Wireless Links use **broadcast**.  Received by all nodes in range.

---

Example Networks

- WiFi(802.11)
- Ethernet(以太网)
- ISP(Internet Service Provider)
- Cable/DSL
- Mobile phone / cellular(2G, 3G, 4G)
- Bluetooth
- Telephone
- Satellite

---

Network names by scale
![](/media/files/2014/07/03/9.bmp)

---
Internetworks(网络)

    + An internetwork or internet 就是把一堆网络联合在一起的网络
    + The Internet是最大的，最常用的internet.

---

Network Boundaries
![](/media/files/2014/07/03/10.bmp)
![](/media/files/2014/07/03/11.bmp)

---

Key Interfaces
![](/media/files/2014/07/03/12.bmp)
![](/media/files/2014/07/03/13.bmp)
![](/media/files/2014/07/03/14.bmp)

---

### 1.4 Sockets
+ Simple abstraction to use the network
+ Support two kinds of network services：streams（流）, datagrams（数据报）

![](/media/files/2014/07/03/15.bmp)
![](/media/files/2014/07/03/16.bmp)
![](/media/files/2014/07/03/17.bmp)

---

### 1.5 Traceroute
&emsp;&emsp;通过探测连续的结点传递消息的方式来找出网络的路径。
![](/media/files/2014/07/03/18.bmp)

---

### 1.6 Protocols and Layers
&emsp;&emsp;协议和分层让网络的使用结构化和模块化。协议实体水平对话，且只用到下一层的服务。

**Encapsulation**
![](/media/files/2014/07/03/19.bmp)

Done with demultiplexing keys in the headers.

Advantages of layering
    information hiding and reuse.

Disadvantages of layering
    Adds overhead and hides information which causes some apps could not get what they want.

### 1.7 Reference Models
OSI Reference Model

&emsp;&emsp;国际标准，功能划分好，但没有在实际中使用。
![](/media/files/2014/07/03/20.bmp)

Internet Reference Model
![](/media/files/2014/07/03/21.bmp)

![](/media/files/2014/07/03/22.bmp)
&emsp;&emsp;网络层使用IP协议，这样传输层、Link层的协议就可以变化很大，只要符合IP协议的接口要求。

---

制定标准的组织
![](/media/files/2014/07/03/23.bmp)

---

一些名词
![](/media/files/2014/07/03/24.bmp)

![](/media/files/2014/07/03/25.bmp)
![](/media/files/2014/07/03/26.bmp)

---

### 1.8 History of the Internet
![](/media/files/2014/07/03/27.bmp)

- ARPANET(packet switching and decentralized control)
- NSFNET(TCP/IP, DNS, Berkeley sockets, BGP)：因PC和以太局域网的出现而大量增长
- Modern Internet：大量的ISPs出现

Modern Internet Architecture
![](/media/files/2014/07/03/28.bmp)
