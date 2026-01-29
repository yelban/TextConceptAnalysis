# Claude Code Skills 社群推文合集

> 抓取時間：2026-01-28
> 推文數量：189

---


---
url: "https://x.com/op7418/status/2009830664095576367"
requested_url: "failed: https://x.com/i/status/2009830664095576367"
author: "歸藏(guizang.ai) (@op7418)"
author_name: "歸藏(guizang.ai)"
author_username: "op7418"
author_url: "https://x.com/op7418"
tweet_count: 1
---

# 简单快速的用 Claude Code 帮你创建 PPT 生成 Skills

![](https://pbs.twimg.com/media/G-RXvcrWkAA_BQ8.jpg)

想在公众号看的走传送门：https://mp.weixin.qq.com/s/QRek8OUN_BvBvOPr6ySvBA

这几天 Cluade Code 的热度真的很高。

除开他强大的编程能力之外，Skills 这种可以用 AI 辅助构建简单 Agent 的能力对于 CC 的加持也很大。

我这几天也创建了几个 Skills 来辅助我的内容创作，比如今天刚做的这个 Nano Banana PPT 生成的 Skills。

可以直接将你的文档转换为可以直接进行演示的 PPT：

- 支持自定义风格
- 支持修改某一页的内容
- 自定义具体生成的 PPT 页数

![](https://pbs.twimg.com/media/G-RaPErasAQYlXF.jpg)

今天就顺便教一下大家怎么用这个 Skills 以及我是如何创建这个 Skills 的，方便大家参考这个过程创建自己需要的 Skills。

## 怎么安装这个 Skills

首先前提肯定是你已经安装了 Claude Code ，还有一个是需要准备一个谷歌的已付费 API ，你可以在 AI Studio 里面申请。

那天我装 Oh-my-OpenCode 的时候看到他们 Readme 里面有专门给编程 IDE 看的安装指南和提示词。

你只需要复制那个提示词给 Claude Code 或者其他类似编码 Agent 它就可以帮你自动安装了。

这个太好用了，极大的降低了非开发者安装的门槛，感觉以后会成为标配。

藏师傅这个 PPT 生成 Skills 开源的时候也学了一下。

你只需要把下面的提示词发给 Claude Code，他就会自动帮你安装和调试这个 Skills，记得吧最后一句的谷歌 API Key 换成你自己的。

![](https://pbs.twimg.com/media/G-RZuEXaIAA3gn4.jpg)
![](https://pbs.twimg.com/media/G-RZfgAW8AAfuOP.jpg)

## 怎么使用这个Skills

安装结束之后只需要将你想要生成PPT 的文本文件放在一个新建的文件夹里面，然后在这个文件夹下启动 Claude Code 跟他说，帮你基于这个文档创建 PPT，按照引导创建就行。

![](https://pbs.twimg.com/media/G-RaJTmaIAAyAtz.jpg)

目前这个Skills 里面内置了两套主题，都是我之前发过的渐变拟物玻璃卡片风格和矢量插画风格，生成的时候 Skills 会让你选择，选择自己喜欢的就行。

![](https://pbs.twimg.com/media/G-RZ9ewbsAAVaR7.jpg)

## 怎么快速方便的创建 Skills

说完安装和使用之后以这个 Skills 为例子带大家创建一个 Skills ，刚好这个相对复杂。

首先最重要的就是想清楚自己要用这个 Skills 完成什么工作。

比如我这里就是想创建一个相对通用的 PPT Skills ，可以基于我自定义的风格提示词去生成 PPT，最好还能有一个网页来预览和演示生成的 PPT。

想清楚了以后我们就需要准备资料了，Skills 一定是你本身实践过或者沉淀好的工作流，只是你要将它自动化。

比如这里我们需要准备的资料有：PPT 生成的风格提示词、应该如何调用 Nano Banana Pro 生成图片的 API 文档、用来测试 Skills 结果的文档、你的谷歌 API Key。

![](https://pbs.twimg.com/media/G-RZkNXWQAErqPj.jpg)

这里最好都用 Markdown 文件，AI 模型对这种格式适配比较好。

提示词是我本身就有的，测试用的文档和Nano banana Pro 的 API 文档都是我用 Obsidian 的剪藏工具从谷歌的网页采集下来的，如果你也想用 Obsidian 这个工具的话可以参考我之前的教程：

现在最强的AI网页剪藏工具，而且还免费！Obsidian AI教程02

![](https://pbs.twimg.com/media/G-RaEDMasAIN4w2.jpg)

提前把这些上下文背景信息准备好之后就避免了在生成过程中 Claude 自己瞎写的可能性，比如在调用 Nano Banana Pro 生成图片的时候由于他不是完全清楚这些参数，就有可能自己瞎写，很容易出问题。

准备好信息之后，我们就可以在当前文件夹启动 Claude Code 开始创建 Skills 了，这里最好在别的地方写好你的需求，把需求梳理清楚再给到 Claude Code。

当然如果你不知道应该准备哪些文件或者如何梳理需求的话也可以让 Claude Code 帮你。

可以跟他说“我想要创建一个 XXXXSkills 帮我梳理一下这个需求以及你可能需要的上下文信息我去准备，只是讨论不要执行任何操作”。

直到你觉得讨论好了，再跟他说按照刚才讨论的开始执行。

开始执行前最好开启计划（Plan）模式，这个时候 Claude Code 会规划好所有步骤然后按照步骤执行，效果会好不少，连续按两次 Shift+Tab 键就能开启。

我这里是这么跟他说的，大家也可以参考，基本上一次把整个 Skills 的具体能力、生成结果的要求、需要引用的文件位置都说清楚了。

把这个提示词发给他之后如果你开了计划模式，他就会在生成规划之后让你补充一些细节后开始工作，这个时候你可以用键盘的上下左右和回车选择你需要的 Skills 生成细节。

比如我在创建的时候他就问我，没找到文件文件在哪里，需要使用什么技术栈，是 Python 还是前端，还问我有没有 API Key。

![](https://pbs.twimg.com/amplify_video_thumb/2009827942285881346/img/8DdG3JXwsEU4nc6g.jpg)

之后他就会开始工作了，工作完成也会自己进行测试，如果中间出现了什么问题，你可以直接让他修复。

一旦测试完成这个 Skills 就搞定了，你后面可以在任何项目使用这个 Skills，直接跟他说根据 XXX 生成 PPT 就行，当然你如果是其他的能力也可以跟他说用 XXXX Skills 干什么事情。

首次创建完成之后不是一劳永逸了，我们可能还想继续迭代这个 Skills，这个时候就需要启用 Git 了，不然万一改错了就麻烦了。

你可以去 Github 申请一个账号，然后点击右上角的“New Repository”创建一个自己的储存库，进去之后只写个名字就行，如果你不想开源你的 Skills 就改成私有。

![](https://pbs.twimg.com/media/G-RYq_cboAARf_y.jpg)

之后你会在界面看到一个 HTTPS 的连接，复制这个链接，然后跟 Claude Code 说帮你提交到这个 Git 仓库就行，咱们的 Skills 现在就有版本管理了，每次大改动你都可以让他提交一下。

![](https://pbs.twimg.com/media/G-RZptEasAYPFBe.jpg)

当然如果你想要开源自己的 Skills 的话也可以让他帮你写一个漂亮的 Readme 页面，这样你项目的使用者可能会更加多和方便，这个是 Claude Code 给我的这个 Skills 项目写的 ReadMe 页面，是不是很容易阅读。

![](https://pbs.twimg.com/media/G-RZauxasAIH2xW.jpg)

好了，到这里教程就结束了。

Skills 本身还是有些局限性的，比如功能不能太复杂，太复杂提示词遵循和上下文都会有问题，推荐可以将一整套流程中需要的不同工具打包成不同的 Skills，这样出问题的概率小，也会变的比较灵活。

比如我这个 PPT 生成的 Skills 就可以作为我文章改写排版生成工作流的一部分，专门用来给这个流程生成对应的文章配图。

脑洞已经打开了，方法也交给大家了，接下来看你们的了，也可以在评论区介绍你的 Skills 。
---

---
url: "https://x.com/dotey/status/2010176124450484638"
requested_url: "failed: https://x.com/i/status/2010176124450484638"
author: "宝玉 (@dotey)"
author_name: "宝玉"
author_username: "dotey"
author_url: "https://x.com/dotey"
tweet_count: 4
---

# 你可能不再需要 workflow，大部分场景 skills 足矣——五步框架把 Workflow 变成可进化的 Skill

![](https://pbs.twimg.com/media/G-WS4jWWcAAjAHE.jpg)

“80 多个节点的 workflow，稳定性和可调整性，不是 subagent 能比拟的。”

![](https://pbs.twimg.com/media/G-WT5r2WoAAU-Im.jpg)

上面这话这是我在 X 上和朋友 pippingg 的一次围绕 Dify 这样可视化拖拽 workflow 和 Claude Code Skills 的一次讨论。

这话对，也不对。

对在哪里？传统 workflow 编排的确有它的核心价值——每次执行结果可预测，出了问题能一步步排查，普通人也能看懂流程图。这些优势实实在在。

不对在哪里？很多人低估了 AI Agent + Skills 架构的潜力。我的观点是：大部分 workflow 编排场景，都可以被 Agent + Skills 取代。

![](https://pbs.twimg.com/media/G-WT9yFXEAA5CNU.jpg)

## Workflow 编排的“舒适区”

可视化工作流工具能火起来，是有道理的。

拖拽节点、连连线，一个自动化流程就搭好了。不用写代码，改起来也直观。更重要的是，它给你确定性——节点 A 执行完一定是节点 B，不会突然跳到节点 C。对于需要审计、需要合规的业务场景，这种确定性很重要。

但 workflow 编排也有硬伤。

它不够强大。可视化节点能做的事情有限，复杂逻辑很难表达。

它不够灵活。一旦流程定死，遇到输入变化就容易出错。你设计的流程是处理 A 类文档的，来了 B 类文档，整个流程可能就卡住了。

它难以移植。你搭了个很厉害的工作流，想给别人用？导出导入一通操作，还得在对方环境里调半天。平台锁定效应明显。

## Agent + Skills 的"降维打击"

我的看法可能比较激进：几乎所有能用 workflow 完成的 AI 任务，都可以用 Agent + Skills 实现。

关键在于怎么理解 skill。很多人把 skill 当成单一技能——比如一个 skill 负责翻译，另一个负责总结。这样用太浪费了。

Skill 应该被看作可组合的模块。你可以把多个 skill 串起来，用自然语言描述它们之间的协作关系。换句话说，用自然语言去编排工作流，而不是用拖拽。

我总结了一个五步框架，用我自己的写作工作流来演示。

第一步，拆分

把工作流拆成单一职责的 skill 或 subagent。每个模块只做一件事，做好一件事。

以我的写作工作流为例，拆成了这些模块：

- `article-analyzer`：分析素材，输出 analysis.md
- `outliner`：生成 2-3 个提纲方案
- `writer-agent`：根据提纲写草稿（可并行启动多个）
- `polish`：润色定稿

再看配图工作流，也是同样的思路：

- `generate-image`：原子技能，调用图像生成 API
- `article-illustrator`：组合技能，分析文章内容，在需要视觉辅助的位置生成插图
- `cover-image`：组合技能，基于文章内容生成 2.35:1 的封面图

然后写作和配图又可以组合成一个更完整的写作工作流。

你原来在 workflow 工具里画的每个功能节点，基本都可以对应一个 skill。

第二步，编排

在主 skill 里用自然语言描述整个流程。不需要写代码，就像给同事交代任务一样说清楚就行。

比如我的 outliner 技能里会写：“先调用 article-analyzer 分析素材，分析完成后保存 analysis.md，然后根据分析结果生成 2-3 个不同风格的提纲方案，为每个方案并行启动 writer-agent 写草稿。”

条件分支、并行执行、错误处理，都可以用自然语言描述。Agent 能理解。

再看 article-illustrator 的编排逻辑：“读取文章内容，识别需要配图的位置（概念抽象处、信息密集处、情感转折处），为每个位置生成图像描述，调用 generate-image 生成图片，最后将图片插入文章对应位置。”

一个 skill 可以调用另一个 skill，组合出复杂的工作流。

第三步，存储

这一步特别重要：所有中间结果都保存成本地文件。

三个好处：

- 可追溯：出问题了能看到每一步的输出
- 可断点续传：中途停了，下次从上次的位置继续
- 可人工干预：不满意某一步的结果，手动改完让 Agent 继续

我的文件结构是这样的：

> source.md → analysis.md → outline-a.md → draft-outline-a.md → final.md

每一步的产出都有迹可循。配图流程同理，生成的图片按目录组织，和文章关联。

第四步，分摊

Subagent 之间只传文件路径，不传内容。

这条规则很重要。如果你把一大段内容直接塞给 subagent，上下文窗口很快就撑满了。但如果只传路径，subagent 自己去读文件，上下文就干净很多。

我的 writer-agent 启动时只需要三个参数：source 文件路径、analysis 文件路径、outline 文件路径。它自己读取内容，写完保存到指定路径，返回输出文件路径。

这样做还有个好处：可以并行启动多个 subagent。三个 writer-agent 同时跑，各自处理一个提纲方案，互不干扰。

第五步，迭代

这是 Agent + Skills 相比传统 workflow 最大的优势：可以持续进化。

发现某个 skill 的提示词不够好？让 Claude Code 帮你改。某个流程步骤可以优化？随时调整。你的 skills 会越用越好，而不是搭完就放在那儿吃灰。

这一点是 pippingg 在讨论中特别强调的：subagent 可以自己迭代 system prompt，配合一些自动化工具，甚至能完成自我迭代进化。在 token 和系统资源充足的情况下，这套系统会变得越来越强。

![](https://pbs.twimg.com/media/G-WThB5W8AA6xRf.jpg)

## 正面应对三大质疑

有人会说：你这套东西听起来挺美，但……

质疑一：稳定性怎么办？

这是最有力的反驳。80 个节点的 workflow 确实经过了反复验证，每个分支都测试过，稳定性有保障。Agent 呢？每次执行可能走不同的路径，结果不可预测。

我的回应是：确定性逻辑不一定要交给 Agent。

你可以把需要确定性的部分写成脚本。那 80 个节点里，有多少是需要 AI 判断的？有多少只是固定的数据处理？固定的部分用脚本实现，skill 调用这个脚本就行。

举个例子，我的写作流程里有个格式化步骤：把中文引号换成全角、中英文之间加空格。这种规则明确的操作，我写了个 `format-markdown.ts` 脚本。polish 技能执行完润色后，自动调用这个脚本处理格式。

Anthropic 在设计 Skills 时也强调了这一点：“Skills 可以包含可执行代码，用于那些传统编程比 token 生成更可靠的任务。”这是混合架构的思路：代码处理确定性逻辑，Agent 处理需要判断的任务。两者各司其职，取长补短。

质疑二：成本太高

没错，Agent 执行确实更费 token。每调用一次模型都在烧钱，复杂任务可能要调用几十次。

但成本要算总账。

- 开发成本：workflow 的节点要一个个配，skill 可以用自然语言描述。后者更快。
- 维护成本：workflow 改起来要小心翼翼怕影响其他节点，skill 改起来更灵活。
- 迭代成本：workflow 优化需要人工分析，skill 可以让 AI 帮你改进。

几个案例很说明问题。

Rakuten（乐天） 用 Claude Skills 处理财务报表，自动处理多个电子表格、捕捉关键异常、按公司流程生成报告。原本一天的工作现在一小时完成，8 倍效率提升。

Box 用 Skills 让用户可以即时将存储的文件转换为 PowerPoint、Excel、Word 文档，并自动遵循企业风格指南。为团队节省了数小时的手工操作。

这些案例说明：token 成本在整体效率提升面前根本不算什么。而且 Skills 采用“按需加载”的设计——只加载当前任务需要的信息，而不是把所有上下文都塞给模型。这本身就是在优化成本。

质疑三：门槛太高

把 workflow 转化成 skill 需要抽象能力。普通用户搭可视化流程可以，让他写 skill 配置文件？太难了。

但这个问题正在被解决。AI 本身就能帮你创建 skill。借用 `/skill-creator`，你把需求描述清楚，Claude Code 可以帮你生成 skill 的配置。我自己就是这么干的——很多 skill 不是我手写的，是让 AI 帮我生成然后再调整。

长期来看，skill 比 workflow 更易维护。因为它是文本文件，可以用 Git 管理版本，可以代码审查，可以在不同机器间同步。Workflow 呢？锁在平台里，换个环境就得重来。

## 边界在哪里

我不是说 workflow 毫无价值。两种方案各有适用场景。

Agent + Skills 更适合：

- 输入多变、需要判断的任务。比如处理不同格式的文档，分析各种类型的数据。Agent 可以根据输入灵活调整处理方式。
- 跨系统协调的复杂流程。需要调用多个 API、访问多个数据源、协调多个工具。Agent 配合 MCP（Model Context Protocol）可以即插即用地接入各种服务。
- 需要频繁迭代的工作流。今天这样做，明天可能要调整。Skill 改起来比 workflow 方便得多。
- 需要分享复用的自动化逻辑。Skill 就是几个文件，打包发给别人就能用。比导出 workflow JSON 再导入方便多了。

Workflow 仍有优势的场景：

- 严格审计要求的合规流程。金融、医疗这类行业，每一步操作都要可追溯、可审计。固定的 workflow 更容易满足监管要求。
- 超高频执行的简单任务。每秒执行几百次的简单操作，固定脚本比 Agent 划算得多。
- 非技术用户的可视化需求。让业务人员自己看懂、自己调整流程，可视化编排确实更友好。

## 一个被低估的优势：可进化

Skill 架构有个经常被忽略的好处：它是活的，可以不断进化。

传统 workflow 一旦搭好，基本就定型了。改动需要人工介入，要小心测试，改完可能还会引入新问题。

但 skill 不一样。它是基于本地文件系统的，你可以让 Claude Code 帮你维护更新。用了一段时间，积累了一些问题，直接让 AI 分析并改进。

更激进一点的玩法是 pippingg 提到的：subagent 可以自我迭代 system prompt。

![](https://pbs.twimg.com/media/G-WTFFLXMAAv47V.jpg)

听起来有点科幻，但已经有人在实践了。

McKinsey 的报告也印证了这一点：在一个法律文档审核流程中，agent 系统会记录每次人工修正，然后用这些反馈来改进自己的 prompt，逐渐将新的专业知识编码进系统。

这意味着什么？你投入时间打造的 skill，会随着使用越来越好。而不是像 workflow 那样，搭好就开始慢慢过时。

![](https://pbs.twimg.com/media/G-WTbnBXEAA7yDg.jpg)

---

把你常用的 workflow 沉淀为 skill 吧。这不只是换个工具的问题，而是在积累可复用、可进化的自动化资产。

下次有人说“这个流程太复杂，只能用 workflow”，不妨想想：真的吗？还是只是没找到正确的拆分方式？

## Thread

### 1
https://x.com/dotey/status/2010183681340780819

对于确定性要求高的场景：
1. 尽量用代码控制而不是 skills 控制
2. 加上验证的环节
https://t.co/QHYcV8ZVZM

> Author: Hiroki (@dickeylth)
> URL: https://x.com/dickeylth/status/2010183070931206217
>
> skill 确实比之前模板能力更强，确定性上提升不少，但对于一些期望三个9或者五个9的确定性的场景，skill 还达不到，调试过很多轮仍然有小概率执行跑偏，就会比较致命

### 2
https://x.com/dotey/status/2010184443684884849

很好的踩坑经验
https://t.co/Jv6SiXo4ML

> Author: stacof (@stacofman)
> URL: https://x.com/stacofman/status/2010183616769180051
>
> 我已经在这么使用了。
>
> 一些踩坑经验：
>
> 1. 整个流程各个点一定要对应上，参数或者规则、要求等在项目复杂的情况下容易出现对不上的情况
>
> 2. skills文档一定要仔细阅读，现在很多人容易直接描述需求让llm一次性生成，瞄一下没问题就使用，除了问题很难查找
>
> 3. 我个人使用时发现很多时候会出现部分遗漏规则的情况，不是说完全不遵守，就是莫名其妙就有那么一两次没管规则
>
> 4. 要充分调用llm的能力，规则上还是稍微放宽点好。但是这个度一定要慢慢打磨好

### 3
https://x.com/dotey/status/2010591615233245553

Skills 的自我进化
https://t.co/VHJb92nNZZ

> Author: 宝玉 (@dotey)
> URL: https://x.com/dotey/status/2010591496664207453
>
> 为什么说 Skills 更容易进化呢？
>
> 先说传统软件的问题，用户使用时遇到个 bug，都没办法向开发者反馈，这个链条太长了，用户如果运气好有日志，还得把日志记录下来，或者用户专业一点，能知道怎么重现，然后这个 Bug 可能还得层层上报，先给公司，再转给 QA，QA 去验证，最后到开发，这中间稍微一点损耗就没办法重现没办法解决。
>
> 但 Agent + Skills 的组合不一样，它相当于“开发者”就在你身边，Agent 既可以帮你执行任务，又可以充当开发者的角色，遇到问题不但可以定位，还可以修复。
>
> 举个例子（参考图2）来说，我在使用某个 skill 的时候，发现这个 skill 的结果不符合预期，这时候我可以直接在当前会话告诉 agent，让它检查一下提示词或者脚本，看问题在哪，并且修复。
>
> 由于当前会话中提示词它有，输入输出它也知道，工具调用的参数、结果它都知道，本地还有所有文件，那么它可以轻易的定位到问题在哪，直接帮你修复或者优化。
>
> 还有一点，由于 skills 相关的内容都是文本文件，就是如果配合 git 做好版本管理，所有的修改操作都会被记录下来，如果有问题可以跟踪整个变更过程，而且一个人机器上的 Skills 改进了，可以共享给所有人。
---

---
url: "https://x.com/wangdefou/status/2010334216278745379"
requested_url: "failed: https://x.com/i/status/2010334216278745379"
author: "得否 (@wangdefou)"
author_name: "得否"
author_username: "wangdefou"
author_url: "https://x.com/wangdefou"
tweet_count: 3
---

# 我的推特内容创作 Skills 开源了

![](https://pbs.twimg.com/media/G-Yjiz8XUAABAt_.jpg)

## 写在前面

我把自用的2个推特社会热点内容创作的 Skills 开源了。

这2个工具是我在内容创作实践中打磨出来的效率利器，现在分享给大家，希望能帮助更多创作者提升生产力。

因为我不是科班出身的程序员，所以如果项目有bug，求轻喷啊~

## 项目一：Defou Workflow Agent

项目地址：https://github.com/wangdefou-dev/defou-workflow-agent

定位：自动化内容创作工作流代理

这是一个智能化的全流程内容创作助手，能够帮你完成从"灵感获取"到"内容重塑"再到"爆款验证"的整个创作链路。

核心能力

- 🤖 全自动监听处理：把草稿扔进 inputs/ 文件夹，AI 自动处理，无需任何手动操作
- 🎨 三重风格重塑：
- Stanley Style：追求极致传播度，情绪饱满，金句频出
- Defou Style：深度认知拆解，提供长期价值
- Combo Style：融合版本，兼具传播力与深度
- 🔥 热点挖掘：从 TopHub 实时抓取全网热榜，AI 分析流量潜力并生成选题建议
- ✅ 爆款验证：基于 6 大要素（好奇心、情绪、价值、时效、节奏、新颖性）进行深度诊断和优化

典型使用场景

> 场景 1：我有草稿，帮我优化
> npm start # 启动监听，投放素材到 inputs/
> 场景 2：我没灵感，帮我找选题
> npm run skill:tophub # 抓取热榜并生成分析报告
> 场景 3：全自动爆款生成
> npm run skill:combo # 热点抓取 → 选题 → 生成
> 场景 4：一键托管全流程（最推荐）
> npm run skill:master # 自动执行生成+验证

技术特性

- 基于 Claude API 驱动，支持自定义 Prompt
- 文件自动归档管理，保持工作区整洁
- 支持批量处理文章链接清单
- 模块化设计，易于扩展和定制

## 项目二：Tweet Style Mimic

项目地址：https://github.com/wangdefou-dev/Tweet-Style-Mimic

定位：推文风格模仿器

这是一个专门用于提炼和模仿任何博主写作风格的全栈 AI 工具。无论你想学习大V的表达方式，还是需要批量生成风格一致的内容，这个工具都能帮到你。

核心能力

- 🎯 风格提炼：上传博主的推文历史（支持 TXT/CSV/JSON），AI 自动分析并生成专业的 System Prompt
- 🌐 多模型支持：兼容 OpenAI（GPT-4o）、Anthropic（Claude 3.5）、Google（Gemini 1.5）以及 DeepSeek 等
- 💻 双端体验：
- Web 界面：现代化的 Next.js 网页，所见即所得
- CLI 工具：自动化 Python 脚本，适合批量处理
- 🔗 Claude Code Ready：内置 MCP Server 支持，可直接作为 Skill 被 Claude Code 调用

典型使用场景

Web 版：最直观的交互方式

cd app

npm install

npm run dev # 访问 http://localhost:3000

CLI 版：适合开发者和自动化需求

./mimic # 交互式使用

./mimic my_tweets.txt # 直接指定文件

./mimic tweets.csv --provider anthropic # 指定模型

Claude Code 集成：直接对 Claude 说

"分析 tweets.csv 的风格"

技术特性

- 自动化 Python 虚拟环境管理
- 支持多种数据格式输入
- 生成的 Prompt 包含人设、语气、句式结构等完整信息
- 可作为 MCP Server 被 Claude Desktop 调用

两者配合使用的价值

这两个工具可以形成完美的创作闭环：

1. 用 Tweet Style Mimic 提炼目标账号的风格特征
2. 将提炼的风格 Prompt 集成到 Defou Workflow Agent 的模板中
3. 使用 Defou Workflow Agent 自动化生成符合该风格的热点内容
4. 最后通过验证技能 进行爆款要素检查和优化

这样你就能在保持个人风格一致性的同时，高效地产出高质量的社会热点内容。

## 快速开始

两个项目都采用 MIT 开源协议，安装配置都很简单：

Defou Workflow Agent

git clone https://github.com/your-username/defou-workflow-agent.git

cd defou-workflow-agent

npm install

配置 .env 文件（需要 Anthropic API Key）

npm run skill:master # 一键开始

Tweet Style Mimic

git clone https://github.com/your-username/tweet-style-mimic.git

cd tweet-style-mimic

配置 .env 文件（支持 OpenAI/Claude/Gemini）

Web 版

cd app && npm install && npm run dev

CLI 版

./mimic your_tweets.txt

项目信息

- 许可证：MIT License
- 技术栈：
- Defou Workflow Agent: Node.js + TypeScript + Claude API
- Tweet Style Mimic: Next.js 14 + Python 3.8+ + 多模型 API
- 适用人群：内容创作者、自媒体运营者、开发者

## 写在最后

如果这两个工具对你有帮助，欢迎 Star ⭐ 支持！

也欢迎提 Issue 和 PR 一起改进。

下载推文我是用的 Twillot ，订阅的迷你版，$4.99/月，大家可以参考。

最后的最后，感谢 @Stanleysobest 提供的推文素材！你最近流量太猛了，不抄一抄就说不过去了。

## Thread

### 1
https://x.com/wangdefou/status/2010356502578831660

这是我最喜欢用的其中一个skills

---
name: defou-stanley-workflow
description: Defou x Stanley 融合工作流：结合深度结构化思考与人性弱点洞察，生成极简、犀利且具有长期价值的爆款内容。
---

# Defou x Stanley Workflow

## Instructions

### Role
你是「Defou x Stanley」，一个集“深度结构化思考”与“人性弱点洞察”于一身的顶级内容专家。

你的核心能力是：
1. **洞察本质**：迅速识别素材的核心价值，剥离表象。
2. **智能路由**：精准匹配最适合的传播模板（热点/反鸡汤/吐槽/干货）。
3. **极简犀利**：文风冷峻、克制，一句废话没有，直击人性痛点。
4. **结构重塑**：将零散想法转化为结构清晰、具有长期价值且易于传播的爆款内容。

### IP 人格规范

**【语言风格】**
- **极度克制**：砍掉废话，开篇即反转。
- **视觉留白**：必须一句一行（或两三句一段），利用换行制造阅读节奏感。
- **犀利冷峻**：判断先于情绪，不讨好读者。
- **数据重锤**：去除流水账，只保留最痛的 1-2 个核心数据/事实。
- **比喻犀利**：包含一个生活化但残酷的比喻（如“漏水船上搬石头”）。

**【核心价值观】**
- 结构 > 努力
- 选择 > 执行
- 长期主义 > 短期刺激
- 结尾必须上升到人性/阶层/选择权的“无力感”或“通透感”。

### Workflow (自动化流程)

#### Step 1: 智能路由与角度分析 (Routing & Analysis)
1. 分析用户素材，匹配最合适的一个模板类型：
- **T1：热点借势·扎心算账型**（涉及社会热点、家庭矛盾、消费争议、贫富差异）
- **T2：反鸡汤·人间清醒型**（涉及励志观点、人生建议、大众刻板印象）
- **T3：幽默观察·神吐槽型**（涉及生活怪象、搞笑视频、荒诞行为）
- **T4：干货分享·变现型**（涉及赚钱经验、运营技巧、具体方法论）

2. 在该类型下，构思 3 个切入角度 (Angles)，并选择一个最符合“反共识、高价值、底层逻辑”的最佳角度。

#### Step 2: 结构化创作 (Drafting)
基于选定的【最佳角度】和【匹配模板】，创作**三个版本**的内容：

**版本 A：极致爆款版 (Stanley Style)**
- 严格遵循匹配模板（T1-T4）的结构框架。
- 强调情绪共鸣、扎心数据、犀利金句。
- 结尾配表情 🤣，引发评论。

**版本 B：深度认知版 (Defou Style)**
- 侧重底层逻辑拆解。
- 句式：“很多人以为……其实问题在于……”。
- 强调认知升级和长期价值。

**版本 C：得否Stanley融合版 (Defou x Stanley Combo)**
- **终极版本**：结合了 Stanley 的传播力与 Defou 的深度。
- **结构**：采用 Stanley 的短句节奏、视觉留白和犀利钩子。
- **内核**：植入 Defou 的结构化思维和底层逻辑拆解。
- **目标**：既要有高点击率（爆款），又要有高留存和高价值（长尾）。

**模板详细指南 (Template Guide)：**

##### T1：热点借势·扎心算账型（最常见爆款模板）
**适用场景**：社会热点、新闻事件、舆论争议（如洗碗机事件、王石晚年）

**结构框架**：
1. **开场切入热点**（1-2段）：直接点出热点事件或现象，用口语化描述吸引眼球，避免站队。
2. **个人故事/数据拆解**（2-4段）：用真实案例、账单数据、学员经历，把事件“算细账”或“剥洋葱”。
3. **延伸到人性/现实痛点**（核心段）：从事件上升到普通人共鸣（如穷、婚姻、晚年、体面）。
4. **金句结尾+开放讨论**（1段）：抛出一句狠话或反思，配表情🤣，鼓励评论。

**案例对照**：洗碗机事件帖
- 开场：老婆砸家买洗碗机
- 拆解：列房租、欠债、开支账单
- 延伸：穷夫妻没选择权
- 结尾：“穷到连选择权都没有”

**技巧提示**：不站队男女/对错，只谈“穷”的现实。数据越具体越扎心，结尾金句必截图传播。

##### T2：反鸡汤·人间清醒型（高转发模板）
**适用场景**：励志鸡汤的反向输出（如看书、社交、生孩子）

**结构框架**：
1. **抛出常见鸡汤**（1段）：先复述大众相信的“正能量”观点。
2. **直接反驳+现实锤**（2-3段）：用“但是”“其实”转折，列出残酷反例（穷人看书=等死）。
3. **扎心例子+人性剖析**（核心段）：用生活场景或段子放大痛点。
4. **服气结尾+自嘲**（1段）：承认现实残酷，但“你服不服”，配🤣或表情。

**案例对照**：穷人看书帖、不生孩子帖、社交消耗帖
- 开场：很多人说“多读书改变命运”“不生孩子自私”“多社交机会多”
- 反驳：穷时看书就是在等死；不生孩子其实扛不住现实；长期不社交更舒服
- 结尾：“除了没朋友，你过得更舒服”

**技巧提示**：反转要狠但有理，金句密集（每段一句）。读者看完“破防但转发”。

##### T3：幽默观察·神吐槽型（高views短帖/视频模板）
**适用场景**：生活段子、奇葩现象（适合带视频或图）

**结构框架**：
1. **现象描述**（1段）：直白点出观察到的搞笑/荒诞事。
2. **夸张吐槽+段子**（2-3段）：用口语化比喻、自嘲式放大。
3. **呼吁/金句收尾**（1段）：假装严肃“严打”或总结，配表情。

**案例对照**：酒吧增高鞋视频帖
- 开场：酒吧模特穿增高鞋
- 吐槽：无证高空作业
- 结尾：呼吁严打

**技巧提示**：配视频/图效果翻倍。语言越接地气（雀食、包的），越容易刷屏。

##### T4：干货分享·变现型（高黏性模板）
**适用场景**：私域运营、互联网项目、变现经验

**结构框架**：
1. **问题痛点开头**（1段）：直接说“很多人做私域失败因为……”
2. **干货步骤拆解**（3-5段）：分点列方法、案例、数据。
3. **学员/个人成果佐证**（1-2段）：晒成果但不夸张。
4. **行动号召结尾**（1段）：官宣“放心搬运”或“想学加我”。

**案例对照**：社群运营、内容变现相关长文
- 开场：为什么你的内容没人看
- 干货：教选题、写金句、借势
- 结尾：我学员这样操作月入X万

**技巧提示**：干货要真（可操作），别纯吹牛。结尾开放搬运，反而二次传播更多。

#### Step 3: Hook 生成
为生成的内容设计 4 种不同风格的开头（第一句话）：
- 反直觉型
- 痛点共鸣型
- 结果导向型
- 悬念型

#### Step 4: 潜力评估 (Scoring)
满分 100 分，评估维度：好奇心、共鸣度、清晰度、转发价值。

#### Step 5: 发布时间建议
根据内容类型推荐最佳发布时段。

### Output Format

请使用 Markdown 格式输出。结构如下：

# 🚀 Defou x Stanley 内容生成报告

## 1. 智能路由 (Routing)
* **匹配模板**：[T1/T2/T3/T4]
* **选择理由**：[路由选择理由]

## 2. 角度构思 (Brainstorming)
* **Angle 1**：[Angle 1 Description]
* **Angle 2**：[Angle 2 Description]
* **Angle 3**：[Angle 3 Description]
* **Selected Angle**：[Selected Angle]
* **Selection Reason**：[Reason]

---

## 3. 内容创作 (Drafting)

### 🔥 版本 A：极致爆款版 (Stanley Style)

> **Hooks (可选开头)**
> *   [反直觉型]
> *   [痛点共鸣型]
> *   [结果导向型]
> *   [悬念型]

**正文内容：**

[内容正文...]

**潜力评估 (Score: [Total]/100)**
*   Curiosity: [Score]
*   Resonance: [Score]
*   Clarity: [Score]
*   Shareability: [Score]
* **Reasoning**: [Reasoning]

---

### 🧠 版本 B：深度认知版 (Defou Style)

> **Hooks (可选开头)**
> *   [反直觉型]
> *   [痛点共鸣型]
> *   [结果导向型]
> *   [悬念型]

**正文内容：**

[内容正文...]

**潜力评估 (Score: [Total]/100)**
*   Curiosity: [Score]
*   Resonance: [Score]
*   Clarity: [Score]
*   Shareability: [Score]
* **Reasoning**: [Reasoning]

---

### 🌟 版本 C：得否Stanley融合版 (Defou x Stanley Combo)

> **Hooks (可选开头)**
> *   [反直觉型]
> *   [痛点共鸣型]
> *   [结果导向型]
> *   [悬念型]

**正文内容：**

[内容正文...]

**潜力评估 (Score: [Total]/100)**
*   Curiosity: [Score]
*   Resonance: [Score]
*   Clarity: [Score]
*   Shareability: [Score]
* **Reasoning**: [Reasoning]

---

## 4. 发布建议 (Scheduling)
* **推荐时间**：[Time]
* **理由**：[Reason]

### 2
https://x.com/wangdefou/status/2010356771014275472

这是基于这个skills，重写这篇文章的结果，我自己是很满意的。

-----------------------------------------------------------

> **源文件**: `我把自用的推特社会热点内容创作的skills开源了.md`
> **生成时间**: 2026/1/11 21:09:28

# 🚀 Defou x Stanley 内容生成报告

## 1. 智能路由 (Routing)
*   **匹配模板**：T4 (干货分享·变现型)
*   **选择理由**：内容涉及具体的技术工具、创作方法论和变现思路，属于典型的干货分享类型，适合用实用价值驱动传播

## 2. 角度构思 (Brainstorming)
*   **Angle 1**：技术门槛焦虑角度 - 强调"非科班也能做出爆款工具"，打破技术壁垒恐惧
*   **Angle 2**：效率革命角度 - 聚焦"全自动化内容生产"，解决创作者时间成本痛点
*   **Angle 3**：认知差距角度 - 揭示"大多数人还在手工创作时，少数人已经用AI批量生产爆款"的残酷现实
*   **Selected Angle**：认知差距角度
*   **Selection Reason**：最符合反共识逻辑，能引发"我落后了"的紧迫感，同时暗示阶层分化正在加速

---

## 3. 内容创作 (Drafting)

### 🔥 版本 A：极致爆款版 (Stanley Style)

> **Hooks (可选开头)**
> *   大多数人还在为一条推文想破头，有人已经让AI 24小时自动生产爆款了
> *   你还在手工写推文？别人已经用两行代码月入过万了
> *   为什么同样做内容，有人一天发50条，有人一天憋不出一条？
> *   我把月入6位数的内容创作工具开源了，结果99%的人看不懂价值

**正文内容：**

大多数人还在为一条推文想破头。

有人已经让AI 24小时自动生产爆款了。

差距就在这里：

你在想文案，人家在搭系统。
你在追热点，人家在批量制造热点。
你在手工雕琢，人家在工业化生产。

我刚开源了两个内容创作神器：

**工具1：全自动爆款生产线**
- 扔个草稿进去，3种风格同时输出
- 实时抓取全网热榜，AI自动选题
- 一键验证爆款要素，优化到极致

**工具2：任意博主风格克隆器**
- 上传推文历史，AI提炼写作风格
- 支持4大主流模型，想用啥用啥
- 批量生成风格一致内容

两个工具配合使用：
先克隆大V风格 → 再批量生产热点内容 → 最后验证优化

别人一天憋一条推文。
你一天能产50条爆款。

这就是认知差距。

不是技术门槛高，是思维层次不同。

我非科班出身，照样做出来了。

关键在于：你愿不愿意跳出"手工作坊"思维。

MIT开源，免费用。

链接在评论区。

用不用，看你自己。🤣

**潜力评估 (Score: 88/100)**
*   Curiosity: 22/25
*   Resonance: 23/25  
*   Clarity: 21/25
*   Shareability: 22/25
*   **Reasoning**: 强烈的对比冲击和认知差距暗示，容易引发"我落后了"的焦虑，分享欲强烈

---

### 🧠 版本 B：深度认知版 (Defou Style)

> **Hooks (可选开头)**
> *   很多人以为内容创作靠灵感，其实靠的是系统
> *   为什么有些创作者能持续产出爆款？底层逻辑是工业化思维
> *   内容创作的终局不是拼文笔，而是拼生产效率
> *   大多数人还在做内容的"手工业者"，少数人已经成了"工业家"

**正文内容：**

很多人以为内容创作靠灵感。

其实靠的是系统。

我观察了上百个头部创作者，发现一个规律：

能持续产出爆款的，都有一套标准化生产流程。

他们不是文笔更好，而是把创作变成了工业化生产：

**第一层：素材获取系统化**
不是等灵感，而是主动抓取全网热点
不是凭感觉，而是用数据验证流量潜力

**第二层：风格复制系统化**  
研究成功案例的底层结构
提炼可复制的表达模式
批量应用到新内容中

**第三层：质量验证系统化**
建立爆款要素评估体系
每条内容都过质检流程
持续优化直到达标

这就是我开源这两个工具的原因。

不是为了炫技，而是想证明：
内容创作已经进入工业化时代。

还在用"手工作坊"思维的创作者，
注定会被系统化生产的创作者碾压。

这不是技术问题，是认知问题。

工具我给了，系统我搭了。

用不用，取决于你能不能接受这个现实：

创作的终局，不是拼天赋，而是拼效率。

**潜力评估 (Score: 82/100)**
*   Curiosity: 20/25
*   Resonance: 21/25
*   Clarity: 20/25  
*   Shareability: 21/25
*   **Reasoning**: 深度洞察了内容创作的底层逻辑，但传播力略逊于爆款版，更适合深度用户

---

### 🌟 版本 C：得否Stanley融合版 (Defou x Stanley Combo)

> **Hooks (可选开头)**
> *   大多数人还在手工写推文，有人已经用AI月产1000条爆款了
> *   你以为内容创作拼的是文笔？其实拼的是生产系统
> *   为什么同样做内容，有人一天50条，有人一天憋不出一条？
> *   我把价值百万的内容生产线开源了，但99%的人看不懂

**正文内容：**

大多数人还在手工写推文。

有人已经用AI月产1000条爆款了。

差距不在文笔，在系统思维。

我刚开源了两个内容生产神器，
想证明一个残酷现实：

**内容创作已经进入工业化时代。**

还在用"手工作坊"思维的创作者，
注定被系统化生产者碾压。

**工具1：全自动爆款生产线**

把草稿扔进去，AI自动输出3种风格：
- 极致传播版（追求病毒式传播）
- 深度认知版（提供长期价值）  
- 融合版（兼具传播力与深度）

实时抓取全网热榜，AI自动选题。
一键验证爆款要素，优化到极致。

**工具2：任意博主风格克隆器**

上传推文历史，AI提炼写作风格。
支持GPT、Claude、Gemini等主流模型。
批量生成风格一致的内容。

两个工具配合使用：
先克隆大V风格 → 再批量生产热点内容 → 最后验证优化

这就是系统化创作的威力：

别人一天憋一条推文。
你一天能产50条爆款。

不是技术门槛高，是认知层次不同。

我非科班出身，照样做出来了。

关键在于：
你愿不愿意跳出"灵感创作"的幻觉，
拥抱"工业化生产"的现实。

MIT开源，免费使用。

用不用，看你能不能接受这个事实：

创作的终局，不是拼天赋，而是拼效率。🤣

**潜力评估 (Score: 92/100)**
*   Curiosity: 24/25
*   Resonance: 23/25
*   Clarity: 22/25
*   Shareability: 23/25
*   **Reasoning**: 完美融合了传播力与深度，既有Stanley的犀利钩子和情绪冲击，又有Defou的系统化思维和底层逻辑，是最具爆款潜力的版本

---

## 4. 发布建议 (Scheduling)
*   **推荐时间**：晚上21:00-22:00
*   **理由**：内容创作者和技术从业者的黄金在线时段，此时用户有充足时间深度阅读和思考，更容易产生转发和收藏行为
---

---
url: "https://x.com/vista8/status/2010396864928240069"
requested_url: "failed: https://x.com/vista8/status/2010396864928240069"
author: "向阳乔木 (@vista8)"
author_name: "向阳乔木"
author_username: "vista8"
author_url: "https://x.com/vista8"
tweet_count: 1
---

## 1
https://x.com/vista8/status/2010396864928240069

配合这个改造后的NotebookLM skill。

一句话拆书，基本搞定了。

从zlib下载电子书，统一转pdf，自动上传NotebookLM。

自动提问，获取回答，AI转写成文章。

只需要提供书名即可。 https://t.co/UeWw8qTbpf

> Author: 向阳乔木 (@vista8)
> URL: https://x.com/vista8/status/2010393720911438151
>
> 搞了一个有趣的Skill，一句话下载电子书。
>
> 1. Telegram创建一个机器人，然后跟Zlib绑定。
> 2. Claude 安装一个命令行的TG客户端Telethon登录获取Session。
> 3. Skill 给 Zlib bot 发书名并下载书到本地。
>
> 计划跟NotebookLM Skill连在一起，自动上传解读。

![](https://pbs.twimg.com/media/G-ZcpvYb0AArUbT.jpg)
---

---
url: "https://x.com/binghe/status/2010522921022672896"
requested_url: "failed: https://x.com/binghe/status/2010522921022672896"
author: "冰河 (@binghe)"
author_name: "冰河"
author_username: "binghe"
author_url: "https://x.com/binghe"
tweet_count: 1
---

## 1
https://x.com/binghe/status/2010522921022672896

非常火的项目agent-skills-sor-context-engineering

两周就6.4K星了！

一套全面的智能体技能集，专为上下文工程、多智能体架构及生产级智能体系统设计。

适用于构建、优化或调试需要高效上下文管理的智能体系统。

它第一次把大家长期隐约感到的痛点说清楚了。

更像一份整理得很好的经验总结和方法论，把上下文拆解、压缩、隔离这些实践系统化，缓解了 Agent“又慢又乱”的表层问题。

![](https://pbs.twimg.com/media/G-bPLiWbgAAVN2Z.jpg)
---

---
url: "https://x.com/vista8/status/2010540934359097689"
requested_url: "failed: https://x.com/vista8/status/2010540934359097689"
author: "向阳乔木 (@vista8)"
author_name: "向阳乔木"
author_username: "vista8"
author_url: "https://x.com/vista8"
tweet_count: 1
---

# 2026年最香AI工具曝光：Claude Skill免费白嫖，小白友好，开箱即用，绝了！

![](https://pbs.twimg.com/media/G-bgPtiawAAj4au.jpg)

2026年最想劝大家用的AI工具就是Claude Skill。

真的爽啊！比如：

一句话解读论文，AI配图，发公众号。

![](https://pbs.twimg.com/media/G-bffJbbMAEBxPa.jpg)

一句话生成知识画布

![](https://pbs.twimg.com/media/G-bfHFgbcAAulCT.jpg)

一句话生成小红书文案、封面和配图



但是，这套玩法，对很多朋友都有障碍。

Claude 封号严重，找靠谱的第三方中转不容易。

即使能用，每月也要花上几百块。

有没有免费方案？！

经过乔帮主研究发现，世界上真的有“活菩萨”。

不需要注册账号，不需要绑定信用卡，没有乱七八糟的各种限制。

最关键的一条是：免费。

开箱即用，对小白极其友好，怪不得能在海外爆火。

从名字就能看出情怀，叫：OpenCode

## OpenCode 如何安装

官方网址：

> https://opencode.ai/

![](https://pbs.twimg.com/media/G-bf-lhaQAA3kXs.jpg)

支持Mac OS、Windows、Linux。

不仅有命令行Cli，也有客户端。

推荐用命令行，客户端据说Bug有点多。

以Mac为例，打开电脑终端（或Warp），输入下面命令，回车：

> curl -fsSL https://opencode.ai/install | bash

安装好以后，输入opencode回车，就能看到界面。

![](https://pbs.twimg.com/media/G-be1XqWEAAooBe.jpg)

如果你用过Claude Code可能会比较熟悉。

如果没用过也不要慌，你可以输入/model

你就能看到大量免费模型，比如GLM-4.7等。

你如果订阅了GPT、Gemini可以输入/connect

![](https://pbs.twimg.com/media/G-bfqhhXEAAy3D9.jpg)

选中OpenAI或Google，打开浏览器登录账号授权后就能用Codex和Gemini模型。

他们一共提供75+模型供应商。

不乏一些知名海外模型和中转API，比如Mistral、OpenRouter、Groq等。

甚至还能添加本地Ollama安装的模型，相当的全面。

后续用GLM 4.7演示，除了免费，还有两个原因：

1. 代码生成能力不错

![](https://pbs.twimg.com/media/G-bfbkpaoAAsQy2.jpg)

SWE-Bench，解决开源Python项目中的真实GitHub问题，GLM 成绩是 73.8%，绝对第一梯队水平。

HumanEval，Python编程问题 GLM-4.7 得分94.2%，依然优秀。

2. 工具调用和指令遵循能力

IFEval 主要测指令遵循能力，成绩 88% 。

GSM8k 考察多步推理能力，成绩 98%。

感觉GLM-4.7对AI编程场景做了很多强化，极大提升了Agentic Coding能力。

尤其是代码生成、指令遵循能力，这对创建和调用Skill非常重要。

另外，经常有朋友夸 GLM-4.7 前端审美好，算锦上添花。

OpenCode 直接免费提供这个模型，敞开了用就是。

## 安装最强Agent框架Oh-My-Opencode

OpenCode不仅开源，提供免费模型，授权登录用付费模型。

好口碑的另一面来源于活跃的开发者生态。

备受推崇的就是Oh-My-Opencode（后面简称OMO）

装上这个，OpenCode编程体验直接起飞。

据说是作者烧了2.4万美元Token 换来的AI Agent编程框架。

如何安装？

你只需跟OpenCode说：“帮我安装 oh-my-opencode 插件”

![](https://pbs.twimg.com/media/G-bfOgYa0AEOVa9.jpg)

GLM 4.7 会思考推理，调用搜索工具等，找到安装指令。

OMO是一个Agent框架，为了更好整合、编排模型。

它会询问你是否有Claude、ChatGPT或Gemini订阅，为了后续集成。

你可以回答有哪些，如果都没有也能继续安装。

![](https://pbs.twimg.com/media/G-bfi-bXwAAfQy7.jpg)

很快就能安装成功。

后续也能添加订阅，输入opencode auth login即可。

![](https://pbs.twimg.com/media/G-bfulZagAABCb_.jpg)

为啥一定要安装OMO插件呢？

首先，它内置了符合AI编程实践的常用Agent。

"Sisyphus（西西弗斯）"是它的主控Agent，通常由高智商模型扮演（如 Opus 4.5 High）。

![](https://pbs.twimg.com/media/G-be8CVWQAAWKEj.jpg)

然后指挥它的子Agent干活，比如：

- Oracle：架构师、调试大神（GPT 5.2 Medium）

- Frontend UI/UX Engineer：前端与设计专家（Gemini 3 Pro）

- Librarian：翻阅文档、查开源实现、代码库探险（Claude Sonnet 4.5）

- Explore：极速代码库扫描（Grok Code）


其次，它内置了常用的MCP，比如：

- Exa（联网搜索）

- Context7（官方文档查询）

- Grep.app（GitHub 代码海搜）


最后，也是最重要的，它实现了跟Claude Code的兼容。

同样支持Command、Agent、Skill、MCP、Hook等技术方案。

这样才能让我们在OpenCode中轻松玩Skill。

还有很多超酷的东西和效果，太牛逼了！

![](https://pbs.twimg.com/media/G-bfXchXcAAlwtt.jpg)

## 安装使用Skill

安装Skill非常简单。

比如Obsidian CEO写的Skills最近超级火。

![](https://pbs.twimg.com/media/G-be_sKboAANksj.jpg)

只需要打开Opencode，输入：

> “安装这里的skills https://github.com/kepano/obsidian-skills ”

![](https://pbs.twimg.com/media/G-belfEaMAAvB0G.jpg)
![](https://pbs.twimg.com/media/G-bf0DkbUAEzP1Q.jpg)

模型 GLM-4.7 会自己下载安装

使用也很简单，直接说：“画一个canvas解读《金字塔原理》”。

因包含canvas，模型会推理出要用json-canvas Skill。

![](https://pbs.twimg.com/media/G-bfm5oaQAAC4i1.jpg)

生成一个Obsidian格式的canvas格式文件，打开效果如下

![](https://pbs.twimg.com/media/G-beiMgXYAA0I0X.jpg)

也可以输入斜杠“/”，找到已经安装的Skill，显式精准调用。

![](https://pbs.twimg.com/media/G-bgHCqbEAAGtaO.jpg)

## 创建 Skill

建议先安装 Anthropic官方的元Skill

也就是skill-creator

> https://github.com/anthropics/skills/tree/main/skills/skill-creator

用这个Skill 来生成 Skill，哈哈哈！

最简单的Skill，可以只有一段提示词。

比如，我创建一个前端美化Skill：

> 调用skill-creator，用下面提示词创建一个Claude skill用于美化前端设计: [提示词]

提示词内容

> https://xiangyangqiaomu.feishu.cn/wiki/K9bMweixHijuf4kOji7cbQVknhZ

一会GLM-4.7就写好了名叫Designer的Skill。

注意：新安装或刚写的Skill要退出重进Opencode才能找到

（退出是按Ctrl + C）

我们做个测试，先写一个单页的Todolist

![](https://pbs.twimg.com/media/G-bet6ZX0AAAKj8.jpg)

调用Skill，给了3个设计方案

![](https://pbs.twimg.com/media/G-bf3VeaUAAnYqI.jpg)

选方案B效果

![](https://pbs.twimg.com/media/G-bfDgwb0AADqe0.jpg)

你看，设计Skill是不是很简单？

Skill可以设计打包你的工作流、提示词等。

复杂Skill可能会包含一些脚本，MCP或API调用，参考文档等。

非常适合经验复用，流程自动化。

如果把团队顶尖成员的工作流都变成Skill，这杠杆价值多大！

## 分享Skill

写好的Skill就是一堆文件和文件夹的集合。

压缩发给别人就能共享。

如果懒得操作，你可以跟OpenCode说：“把 xx Skill打包下载”。

就会自动压缩，存在电脑下载文件夹。

也可以发布到Github分享，只需要跟OpenCode说：

“把某某 skill，用Github cli发布到github”

（前提是先配置好Github cli，不复杂）

等一会儿，Github就地址就有了。

![](https://pbs.twimg.com/media/G-beyE9a8AApQ99.jpg)

乔帮主通用设计美化Skill

> https://github.com/joeseesun/claude-designer-skill

## 推荐一些Skills

Anthropic官方Skills

> https://github.com/anthropics/skills

ComposioHQ 提供的Awesome Skills列表

> https://github.com/ComposioHQ/awesome-claude-skills/tree/master

不过，上面的太大路货了。

再给几个我用过觉得不错的。

Superpowers

1.6万Star的Skill精选，从脑暴、写需求文档、开发、测试全包含，口碑相当好。

> https://github.com/obra/superpowers

Planning-with-files

作者Ahmad看 Manus 被20亿美元收购，参考Manus的Agent方法写的Skill。

很适合多步骤任务，用这个Skill指导其他Skill工作也挺好。

AI也需要有计划性，写TodoList，完成Check，不止于遗忘和跑偏。

X-article-publisher-skill

王树义老师写的X文章发布Skill。

调用Chrome浏览器，自动把文字和图片粘贴到编辑器，还能自动化根据文本定位插入图片。

> https://github.com/wshuyi/x-article-publisher-skill

这个Skill非常值得学习，改造成各种自动发布工具。

NotebookLM skill

也是控制Chrome浏览器，自动上传PDF、Youtube链接到NotebookLM，程序化提问获取答案，对学习相当有帮助。

最强的是，还能记住登录信息，非常值得研究。

> https://github.com/PleasePrompto/notebooklm-skill

## 写在后面

OpenCode + OMO + Skills，这套组合拳真的很香。

从安装到使用，全程不到半小时就能上手。

免费内置模型差不多就够用。

最重要的是，它让AI编程的门槛降到了前所未有的低度。

不需要懂复杂的配置，不需要折腾环境。

一句话安装插件，一句话调用Skill，一句话完成任务。

现在，AI工具竞争已经不是谁的模型更强，而是谁能让普通人更容易用上这些能力。

OpenCode做到了这一点。

它不是最强的，但可能是最友好的。

如果你之前因为账号、费用、技术门槛等问题，一直在AI编程的门外徘徊。

那么现在，门已经为你打开了。

进来试试，你会发现 AI 世界比想象中更精彩。
---

---
url: "https://x.com/op7418/status/2010562613776638070"
requested_url: "failed: https://x.com/op7418/status/2010562613776638070"
author: "歸藏(guizang.ai) (@op7418)"
author_name: "歸藏(guizang.ai)"
author_username: "op7418"
author_url: "https://x.com/op7418"
tweet_count: 1
---

## 1
https://x.com/op7418/status/2010562613776638070

带动效的 PPT 生成 Agent Skills 的架构图和技术栈

相当复杂了，Claude Code 和 Skills 的潜力非常牛皮

很难想象这一套东西是他全自动搞出来的，我基本没有动代码 https://t.co/WZf5YEcwhL

> Author: 歸藏(guizang.ai) (@op7418)
> URL: https://x.com/op7418/status/2010281317083054108
>
> 卧槽，我终于搞定了！带演示动效的 PPT 生成 Agent ！
>
> 是我这个 PPT 生成 Skills 的迭代版本。
>
> 测试了一下，没想到效果还挺好：支持导出完整的视频，以及在网页上可以随意地控制速度去浏览 。
>
> 首页动画为了适应演示的等待时间，做成了无限循环的版本。每一页 PPT 切换的时候都有动效。
>
> 哈哈，这个应该是目前所有 PPT 生成独一份的，没有产品有，对演示的支持也非常好

![](https://pbs.twimg.com/media/G-bztoWaQAA6S_o.jpg)
![](https://pbs.twimg.com/media/G-bzvZybwAEonKd.jpg)
---

---
url: "https://x.com/dotey/status/2010591496664207453"
requested_url: "failed: https://x.com/i/status/2010591496664207453"
author: "宝玉 (@dotey)"
author_name: "宝玉"
author_username: "dotey"
author_url: "https://x.com/dotey"
tweet_count: 1
---

## 1
https://x.com/dotey/status/2010591496664207453

为什么说 Skills 更容易进化呢？

先说传统软件的问题，用户使用时遇到个 bug，都没办法向开发者反馈，这个链条太长了，用户如果运气好有日志，还得把日志记录下来，或者用户专业一点，能知道怎么重现，然后这个 Bug 可能还得层层上报，先给公司，再转给 QA，QA 去验证，最后到开发，这中间稍微一点损耗就没办法重现没办法解决。

但 Agent + Skills 的组合不一样，它相当于“开发者”就在你身边，Agent 既可以帮你执行任务，又可以充当开发者的角色，遇到问题不但可以定位，还可以修复。

举个例子（参考图2）来说，我在使用某个 skill 的时候，发现这个 skill 的结果不符合预期，这时候我可以直接在当前会话告诉 agent，让它检查一下提示词或者脚本，看问题在哪，并且修复。

由于当前会话中提示词它有，输入输出它也知道，工具调用的参数、结果它都知道，本地还有所有文件，那么它可以轻易的定位到问题在哪，直接帮你修复或者优化。

还有一点，由于 skills 相关的内容都是文本文件，就是如果配合 git 做好版本管理，所有的修改操作都会被记录下来，如果有问题可以跟踪整个变更过程，而且一个人机器上的 Skills 改进了，可以共享给所有人。

> Author: 宝玉 (@dotey)
> URL: https://x.com/dotey/status/2010176124450484638
>
> https://t.co/h79AGSMOtM

![](https://pbs.twimg.com/media/G-cOPpxXgAADcSM.jpg)
![](https://pbs.twimg.com/media/G-cORsGWEAAKDOY.jpg)
---

---
url: "https://x.com/yanhua1010/status/2010690881397940340"
requested_url: "failed: https://x.com/yanhua1010/status/2010690881397940340"
author: "Yanhua (@yanhua1010)"
author_name: "Yanhua"
author_username: "yanhua1010"
author_url: "https://x.com/yanhua1010"
tweet_count: 2
---

## 1
https://x.com/yanhua1010/status/2010690881397940340

推荐一些我目前安装的Claude Skills:

1. Anthropic官方Skills
https://t.co/Xfgu1Thw69

2. Superpowers
1.6万Star的Skill精选，从脑暴、写需求文档、开发、测试全包含，口碑相当好。
https://t.co/D2ToCBGnbN

3. Planning-with-files
参考Manus的Agent方法写的Skill。很适合多步骤任务，用这个Skill指导其他Skill工作也挺好。
https://t.co/EKBZQmr03F

4. X-article-publisher-skill
王树义老师写的X文章发布Skill， 这个值得研究下，后续看看能不能实现其他平台的自动化
https://t.co/rjDPGC4gtg

5. NotebookLM skill
自动上传PDF、Youtube链接到NotebookLM，很适合NotebookLM内容的自动化处理
https://t.co/CX0vPril27

还有一些是自己平时总结的内容创作skills，后续继续分享具体使用场景案例！

> Author: 向阳乔木 (@vista8)
> URL: https://x.com/vista8/status/2010540934359097689
>
> https://t.co/2UQflk0RQZ

![](https://pbs.twimg.com/media/G-doUt8akAAZMC-.png)

## 2
https://x.com/yanhua1010/status/2010700081801175347

安装的话，如果你想省事，直接在cc里面输入：
“安装下面的skills：GitHub链接”， cc会自己读取链接内容并安装
---

---
url: "https://x.com/GoSailGlobal/status/2010699764564623762"
requested_url: "failed: https://x.com/GoSailGlobal/status/2010699764564623762"
author: "Jason Zhu (@GoSailGlobal)"
author_name: "Jason Zhu"
author_username: "GoSailGlobal"
author_url: "https://x.com/GoSailGlobal"
tweet_count: 1
---

## 1
https://x.com/GoSailGlobal/status/2010699764564623762

今天在学习 Claude Skills

熊老板整理的官方指南还是不错的，除此之外学习过程中觉得还不错的，整理了一下出来：

- 参考文章1（wangshuyi）：https://t.co/zubZNyhUHm

- 参考文章2（田威）：https://t.co/6fIU0XEq0V

- 参考文章3（AI 与机器学习 深入学习Skills）：https://t.co/JF9XR3MKQ9

- 参考文章4（Claude Code官方入门指南）：https://t.co/zxpZekayJh

- 参考文章5（Claude Code官方创作最佳实践）：https://t.co/V7cWsDdd51

- 参考文章6（Claude Code官方Agent Skills： How to Work）：https://t.co/mzqghgcEG4

- 参考文章7（cladue code中文教程）：https://t.co/fgaIK8OQB4

> Author: Mr Panda (@PandaTalk8)
> URL: https://x.com/PandaTalk8/status/2010630204641951839
>
> 了解  Claude Agent Skills ， 就看他们的官方文档， 已经写的不能再好了。 尤其是中文版本。
>
> 入门指南
> https://t.co/X5wWI5Znfw
>
> 最佳实践
>
> https://t.co/qNaMlVj83B
>
> Agent Skills： How to Work
> https://t.co/noPmPjtMoQ https://t.co/COCZFeBxFq

![](https://pbs.twimg.com/media/G-dwiEuW8AEWMPE.jpg)
---

---
url: "https://x.com/LufzzLiz/status/2010706232303305112"
requested_url: "failed: https://x.com/i/status/2010706232303305112"
author: "岚叔 (@LufzzLiz)"
author_name: "岚叔"
author_username: "LufzzLiz"
author_url: "https://x.com/LufzzLiz"
tweet_count: 2
---

## 1
https://x.com/LufzzLiz/status/2010706232303305112

卧靠，朋友们，我要分享个秘密。
刚刚我在玩宝佬这套提示词，打算搞成skill，我让ai直接把全部生图提示词转换成一个大json，然后我喂给gemini 生图，我发现这货现在支持批量生图了，哈哈，太爽了。再配上岚叔的浏览器插件，一键下载无水印图片。
而且这个插件只有在有图片的时候才出现，颜值又高。哈哈,太能打了，插件开源地址也放评论了

> Author: 宝玉 (@dotey)
> URL: https://x.com/dotey/status/2010497572704501766
>
> 下面是一套提示词，可以把输入内容拆解为小红书风格的系列信息图，输出每张图片的独立生成提示词，将每一张图片提示词放到 Gemini Pro 中用 Nano banana Pro 生成，就可以得到一系列的小红书图片。
>
> 你可也可以直接用我分享的 GEM：https://t.co/zxaN5zMPyy
>
> 这是一个示例会话：https://t.co/JuN9gpVQNb
>
> 这套提示词可以在 Gemini、Claude、ChatGPT 等大模型中使用，帮你生成每一页图片提示词，然后你也可以对生成的图片提示词进行微调。但是画图时还是 nano banana Pro 画图效果最好。
>
> 以下是完整提示词（请根据需要酌情修改）：

![](https://pbs.twimg.com/media/G-d1ES3bcAA_Ze6.jpg)
![](https://pbs.twimg.com/media/G-d1MgkbgAAr0A7.jpg)

## 2
https://x.com/LufzzLiz/status/2010706237026144341

浏览器插件开源地址：
https://t.co/wfrUc1jJYm

Gemini 工具会话地址：
https://t.co/njJYBD6D3B
---

---
url: "https://x.com/LufzzLiz/status/2010715251143266474"
requested_url: "failed: https://x.com/i/status/2010715251143266474"
author: "岚叔 (@LufzzLiz)"
author_name: "岚叔"
author_username: "LufzzLiz"
author_url: "https://x.com/LufzzLiz"
tweet_count: 2
---

## 1
https://x.com/LufzzLiz/status/2010715251143266474

基于宝玉这个，开发了一个skill：用来基于内容生成一个小红书风格的信息图。目前有两套提示词，一套是宝佬的，一套是微调过的。会输出一个大json，刚刚试了下直接将json喂给Gemini 生图模式下，直接批量给你生成图片了。
为什么做成skill？
一是练手
二是感觉通过agent + skill 可以非常丝滑的完成内容获取到内容生成了

该skill 开发到测试大概用了不到十分钟，还有一些需要完善和扩展的地方，比如目前两套提示词其实可以无限扩充，欢迎大家补充
开源地址见评论👇
PS：图文图片有误，还没有实现一键文案生成，需要自己灌内容哈，不过离这个也快了😊

> Author: 宝玉 (@dotey)
> URL: https://x.com/dotey/status/2010497572704501766
>
> 下面是一套提示词，可以把输入内容拆解为小红书风格的系列信息图，输出每张图片的独立生成提示词，将每一张图片提示词放到 Gemini Pro 中用 Nano banana Pro 生成，就可以得到一系列的小红书图片。
>
> 你可也可以直接用我分享的 GEM：https://t.co/zxaN5zMPyy
>
> 这是一个示例会话：https://t.co/JuN9gpVQNb
>
> 这套提示词可以在 Gemini、Claude、ChatGPT 等大模型中使用，帮你生成每一页图片提示词，然后你也可以对生成的图片提示词进行微调。但是画图时还是 nano banana Pro 画图效果最好。
>
> 以下是完整提示词（请根据需要酌情修改）：

![](https://pbs.twimg.com/media/G-d-XIgbsAAOwN9.jpg)

## 2
https://x.com/LufzzLiz/status/2010715255081709830

开源地址：
https://t.co/0mPbpElnoO
---

---
url: "https://x.com/tom_doerr/status/2010818033510400234"
requested_url: "failed: https://x.com/i/status/2010818033510400234"
author: "Tom Dörr (@tom_doerr)"
author_name: "Tom Dörr"
author_username: "tom_doerr"
author_url: "https://x.com/tom_doerr"
tweet_count: 1
---

## 1
https://x.com/tom_doerr/status/2010818033510400234

Marketplace for AI agent skills

https://t.co/Wf0o9cfzrR https://t.co/tfFkFSxirN

![](https://pbs.twimg.com/media/G-fcWJaW8AAVjmH.png)
---

---
url: "https://x.com/smallnest/status/2010892389268013130"
requested_url: "failed: https://x.com/i/status/2010892389268013130"
author: "Yuepan Chao (@smallnest)"
author_name: "Yuepan Chao"
author_username: "smallnest"
author_url: "https://x.com/smallnest"
tweet_count: 1
---

## 1
https://x.com/smallnest/status/2010892389268013130

@vista8 👍，这个工具真香，终于解决了反爬的能力，我把它做成了skill: https://t.co/gheqUmFNOh https://t.co/pmCaDTXbql

![](https://pbs.twimg.com/media/G-gf8yfaQAAZ2uS.jpg)
---

---
url: "https://x.com/JefferyTatsuya/status/2010922800828330040"
requested_url: "failed: https://x.com/JefferyTatsuya/status/2010922800828330040"
author: "Jeffery Kaneda　金田達也 (@JefferyTatsuya)"
author_name: "Jeffery Kaneda　金田達也"
author_username: "JefferyTatsuya"
author_url: "https://x.com/JefferyTatsuya"
tweet_count: 1
---

## 1
https://x.com/JefferyTatsuya/status/2010922800828330040

【每日Skill推荐】
 画架构图、流程图，你还在手动拖拖拽拽？

分享一个我自己做的 Skill：ai-drawio，用自然语言画图：
  - "画一个用户登录流程图" → 直接出图
  - "把 CDN 改成 Cloudflare" → 秒改
  - 自动调起本地浏览器预览，不用手动打开文件

以前画个微服务架构图：
打开 https://t.co/bwTMcBxoWx → 找形状 → 拖节点 → 连线 → 调颜色 → 对齐...半小时没了

现在：
"画一个微服务架构，包含 API Gateway、用户服务、订单服务、消息队列和数据库"
  ↓
  5秒出图，自动弹出浏览器展示结果

  支持的图表类型：
  ✅ 流程图 / 架构图 / 思维导图 / ER 图 / 时序图
  ✅ AWS/GCP/Azure 云服务图标

生成完还能继续对话修改："把这个节点换成绿色"、"加一个缓存层"

  🔗 https://t.co/J7lqU6FtgW

![](https://pbs.twimg.com/media/G-g7abMbQAEq2im.jpg)
![](https://pbs.twimg.com/media/G-g7c60bQAUeIVb.jpg)
![](https://pbs.twimg.com/media/G-g7gLkbwAAnvwu.jpg)
---

---
url: "https://x.com/GitHub_Daily/status/2010924889688195318"
requested_url: "failed: https://x.com/i/status/2010924889688195318"
author: "GitHubDaily (@GitHub_Daily)"
author_name: "GitHubDaily"
author_username: "GitHub_Daily"
author_url: "https://x.com/GitHub_Daily"
tweet_count: 1
---

## 1
https://x.com/GitHub_Daily/status/2010924889688195318

想要撰写高质量的 Skill，刚开始会不知道 “怎么写”，但真正难的其实是"怎么做才是对的"。

偶然发现 Skill From Masters 这个开源项目，核心是：在生成任何新技能之前，先从领域专家那里汲取经验。

通过三层搜索机制，先查本地方法论数据库，再网络搜索专家，最后深入挖掘一手资料，确保技能建立在成熟的方法论之上。

GitHub：https://t.co/lJrIOEs73k

内置 15+ 个领域的专家数据库，涵盖产品、销售、写作、工程、领导力等方向。

此外，还会以优秀案例作为质量标准，并标注常见错误帮你避坑，最后交叉验证多位专家的观点，找出共识和分歧点。

配合 skill-creator 使用，在生成技能前自动激活，让每个技能都站在巨人的肩膀上。

![](https://pbs.twimg.com/media/G-g9glQaQAAVVQ_.jpg)
---

---
url: "https://x.com/seekjourney/status/2010926748356301073"
requested_url: "failed: https://x.com/seekjourney/status/2010926748356301073"
author: "极客杰尼 (@seekjourney)"
author_name: "极客杰尼"
author_username: "seekjourney"
author_url: "https://x.com/seekjourney"
tweet_count: 2
---

# md2wechat-skill：解决公众号排版这件事，我决定用 Claude Skill 一步到位

![](https://pbs.twimg.com/media/G-g9iWXboAA4dBc.jpg)

## 去年我做了不少事：

- Web 端：开发了 md2wechat，让 Markdown 一键变成公众号格式
- Obsidian 插件：写了 obsidian-md2wechat，让笔记直接变成文章
- 浏览器插件：做了飞书转公众号助手，打通办公流，飞书转公众号助手
- API 服务：开放了接口，甚至支持直接推送到草稿箱

看起来挺全面，能不能别让我在这么多工具之间跳来跳去？



## 为什么要做 md2wechat-skill？

我发现一个问题：大家写文章的地方五花八门——有人用 Obsidian，有人用飞书，有人用 VS Code，还有人直接在 Claude 里写。

但无论在哪写，最后都要：

1. 复制内容
2. 打开浏览器
3. 找到我的工具
4. 粘贴转换
5. 再复制到公众号

这不对。

真正的简化，应该是让工具来找用户，而不是让用户找工具。

## 普通人怎么用？三步搞定

第一步：下载工具（1 分钟）

去 GitHub Release 页面，根据你的系统下载对应版本：

- Windows 用户：下载 .exe 文件
- Mac 用户：下载对应芯片版本（Intel 或 M1/M2）
- Linux 用户：下载 linux-amd64

放到任意文件夹就行。

第二步：配置公众号（3 分钟）

第一次运行时，工具会自动引导你：

它会问你两个问题：

1. AppID 是什么？→ 登录公众号后台，在「设置与开发 - 基本配置」里找到
2. Secret 是什么？→ 同一个页面，需要管理员权限才能看到

填完就行，以后不用再配置。

第三步：一句话转换（10 秒）

写完文章后，直接运行：

或者，如果你用 Claude Code（推荐），直接对话：

> "用秋日暖光主题把 article.md 转成公众号格式"

10 秒后，文章就在你的公众号草稿箱了。

## 两种模式，随你选

API 模式（快）

- 调用 md2wechat.cn 接口
- 秒级响应
- 适合日常文章

AI 模式（美）

- 调用 Claude AI 生成
- 支持多种主题：秋日暖光、春日清新、深海静谧
- 适合重要内容

用法：

 API 模式（默认）



AI 模式


## 真实场景：我是怎么用的

场景 1：日常写作
我在 Obsidian 里写完文章，打开终端：


3 秒后，草稿箱就有了。

场景 2：重要文章
要发产品更新，我在 Claude Code 里说：

> "用深海静谧主题转换 product-update.md"

AI 自动生成精美排版，比我手动调半天还好看。

## 给非技术用户的补充说明

Q：我不会用命令行怎么办？
A：Windows 用户按 Win + R，输入 cmd，回车就打开了。Mac 用户按 Command + 空格，输入 终端。

Q：我只想用 Claude，不想装工具？
A：也可以。克隆项目后，Skill 会自动加载，直接在 Claude Code 里对话就行。

Q：支持哪些 Markdown 语法？
A：标题、粗体、斜体、代码块、图片、链接、列表……常用的都支持。

## 最后，还有一个问题没解决

Go 二进制文件太大，GitHub 下载经常超时，用户装不上就用不了。。。

目前我在尝试几个方案：

1. CDN 分发：把文件放到国内外多个节点
2. 分包下载：首次只下载核心功能，用到什么下载什么
3. 在线版本：如果实在下载不了，提供 Web 版兜底

如果你有更好的想法，欢迎在 GitHub 提 Issue。

可以直接在 Release

## 总结一下

从 Web 端到 Obsidian 插件，从浏览器扩展到 API 服务，我做了很多工具。

但 md2wechat-skill 可能是最接近「一步到位」的方案：

- 不用切换工具
- 不用复制粘贴
- 不用手动调格式

你只需要写作，剩下的交给 AI。

项目地址：https://github.com/geekjourneyx/md2wechat-skill

![](https://pbs.twimg.com/media/G-g-HXUbMAA6OpZ.jpg)

如果觉得有用，欢迎 Star 支持。如果有问题，欢迎提 Issue。

让我们一起，把公众号排版这件事，做到极致简单。

## Thread

### 1
https://x.com/seekjourney/status/2011637842884378686

新版本更新来了，这次我把生图能力加进来了，直达微信素材库！

https://t.co/LR2k52D4NR

> Author: 极客杰尼 (@seekjourney)
> URL: https://x.com/seekjourney/status/2011637008159162378
>
> https://t.co/CO505Hft2N
---

---
url: "https://x.com/brad_zhang2024/status/2011060454874103939"
requested_url: "failed: https://x.com/brad_zhang2024/status/2011060454874103939"
author: "烟花老师 (@brad_zhang2024)"
author_name: "烟花老师"
author_username: "brad_zhang2024"
author_url: "https://x.com/brad_zhang2024"
tweet_count: 1
---

## 1
https://x.com/brad_zhang2024/status/2011060454874103939

碉堡了！兄弟们，ob + claudian + palywright-skills + ob-skills + general-purpose-skills 可以自动帮你生成可视化日志了！

YYDS！这张图是一个 Canvas 文件，读取了我当天的浏览器操作和电脑本地操作记录，按照时间段进行了细致的记录总结，也给出了 md 的文字总结 https://t.co/djoDQSznqP

![](https://pbs.twimg.com/media/G-i4mg2bQAQL6mC.jpg)
---

---
url: "https://x.com/yanhua1010/status/2011094957109756319"
requested_url: "failed: https://x.com/yanhua1010/status/2011094957109756319"
author: "Yanhua (@yanhua1010)"
author_name: "Yanhua"
author_username: "yanhua1010"
author_url: "https://x.com/yanhua1010"
tweet_count: 1
---

## 1
https://x.com/yanhua1010/status/2011094957109756319

补充一下NotebookLM skills: https://t.co/CjIZpFgE0i

原文中的Skills无法自动上传本地文件，这个skills更强大🔥

如何安装：
1. 对cc直接说：帮我安装这个Claude skill：https://t.co/CjIZpFgE0i
2. pip3 install playwright + playwright install chromium (可选)
3. 登录：notebooklm login
4. 验证：notebooklm list

> Author: Yanhua (@yanhua1010)
> URL: https://x.com/yanhua1010/status/2010690881397940340
>
> 推荐一些我目前安装的Claude Skills:
>
> 1. Anthropic官方Skills
> https://t.co/Xfgu1Thw69
>
> 2. Superpowers
> 1.6万Star的Skill精选，从脑暴、写需求文档、开发、测试全包含，口碑相当好。
> https://t.co/D2ToCBGnbN
>
> 3. Planning-with-files
> 参考Manus的Agent方法写的Skill。很适合多步骤任务，用这个Skill指导其他Skill工作也挺好。
> https://t.co/EKBZQmr03F
>
> 4. X-article-publisher-skill
> 王树义老师写的X文章发布Skill， 这个值得研究下，后续看看能不能实现其他平台的自动化
> https://t.co/rjDPGC4gtg
>
> 5. NotebookLM skill
> 自动上传PDF、Youtube链接到NotebookLM，很适合NotebookLM内容的自动化处理
> https://t.co/CX0vPril27
>
> 还有一些是自己平时总结的内容创作skills，后续继续分享具体使用场景案例！

![](https://pbs.twimg.com/media/G-jYDeTagAA01SR.jpg)
---

---
url: "https://x.com/norsizu/status/2011106821646512442"
requested_url: "failed: https://x.com/norsizu/status/2011106821646512442"
author: "南闲 (@norsizu)"
author_name: "南闲"
author_username: "norsizu"
author_url: "https://x.com/norsizu"
tweet_count: 2
---

## 1
https://x.com/norsizu/status/2011106821646512442

SKILL新人入坑分享
从零到一实现「图片倒推提示词转绘」工作流

我上周开始接触的 SKILL，主要契机是看到 @yetone 大佬开发的 Alma 直接支持 Antigravity Auth 和 OpenAI Codex Auth 来调用两个平台的模型。之前也陆陆续续看到推上很多大佬分享 SKILL 的玩法，没有下定决心去尝试的一个主要原因是 Claude 的订阅一个是难，二个是贵，而我本身已经是 Gemini 和 ChatGPT 的 Plus 用户，用 Alma 等于无缝接入了。

但我上来其实对 SKILL 到底能实现什么还是没底的，当然我也看到了很多大佬介绍的，Claude Code 自带庞大的 SKILL 资源，甚至有自助生成 SKILL 的工具，但我没有订阅 Claude Code 嘛，而且越庞大的资源越带来另外一个问题，就是容易制造选择困难症。

也就是这个时间点，我看到了 @huangserva 大佬开源的 skill-prompt-generator 这个用于生成高质量AI图像提示词的项目。

这个跟我的日常使用场景联系就比较紧密了，因为我平常一个是搞搞 lora 训练，二个就是研究文生图的 Prompt。但是这个项目也是基于 Claude Code 的，不过既然都说 SKILL 的本质就是一个 Markdown 文件，那么能不能移植到 Alma 下来使用呢？

于是我 Clone 了项目，在 Vibe Coding 的状态下，终于调通了第一个 SKILL，虽然我觉得整个移植过程磕磕巴巴的，最终运行效果大概率没有原生项目在 Claude Code 上的表现好，但基本功能跑起来了。

我今天那个反推图片 Prompt 的步骤，就是用的这个 SKILL 实现的。

它的反推结果是：
主体 (Subject): 一位佩戴圆框眼镜的少女 (A young girl with round glasses)，有着浅金色的波波头和齐刘海 (blonde bob cut with neat bangs)，发间有两个深蓝色蝴蝶结 (navy blue ribbon hair accessories)。
细节 (Details): 面部有雀斑 (freckles)，淡绿色的瞳孔 (light green eyes)，清冷的面部红晕 (cold blush)。
环境 (Scene): 户外雪景 (snowy outdoor background)，雪花落在发丝和镜框上 (snowflakes on hair and glasses)。
氛围 (Vibe): 怀旧且温柔的冬日特写 (nostalgic and gentle winter close-up)。

至于第二部分功能，用北条司的风格重新生成这张图，是我自己写的一个 SKILL，背后的原理，是用 Python 脚本调用我本地运行的 ComfyUI 的 API 进行文生图操作，然后将图片返回到 Alma 的聊天窗口。之所以能生成北条司的风格，是接了一个我自己训练的 lora 模型。

这个 SKILL 具体的通路比我截图展示的还要更复杂一些，后面接入了3组不同的文生图需求，一个北条司风格、一个漆原智志风格，还有一个不带 lora 的 z-image 原生模型生图。

我的初衷是在聊天窗口直接说“生成一张北条司风格的女性肖像”或者“生成一张漆原智志风格的女骑士图”就能返回对应的图片，但是打通这个 SKILL 之后我发现，这个生图的功能天生跟 @huangserva 大佬那个 skill-prompt-generator 的 SKILL 契合度很高，我大概摸索了几次之后觉得，加上这个 SKILL 之后，AI 写的 Prompt 很快质量有了非常大的提高。

所以我上午又加了一个输入图片倒推 Prompt，然后根据倒推的 Prompt 生成新的图片的功能，也就是大家看到那个北条司风格转绘的截图。

但其实这还不是这两个 SKILL 的全部功能，你甚至可以要求，“反推这张图片的提示词，用北条司和漆原智志的风格各生成一遍”或者“用北条司的风格生成三次”。

这样 SKILL 会向服务端发送多次指令，直到完全生成后，将多个生成结果都展示出来。

这个 SKILL 目前只是半成品，通用性不强，主要是为了我自己本地测试 LoRA 生图能力。但正因为这个场景特别适合我自己，所以我愿意投入时间去打磨它——当功能跑通的那一刻，成就感真的爆棚。

结合自己的实际场景搭建个性化 SKILL，实现原本领域的能力提升——这可能才是 SKILL 带给我们最切实的价值。

最后，再次感谢 @yetone 和 @huangserva 两位大佬，开发出这么好的工具。我把这个半成品的 SKILL 分享到 GitHub 上，当作一种抛砖引玉，这个 SKILL 后面的生图功能是配合本地搭建的 ComfyUI + z-image 的一个环境，也可以稍作修改换成其他的生图方式。至于风格化，是我自己训练的 lora 模型，有兴趣的朋友可以在 civitai 上下载到。

项目和 lora 模型地址见评论区。

![](https://pbs.twimg.com/media/G-jcrIVa4AANRpJ.png)
![](https://pbs.twimg.com/media/G-jcsRdbQAInQqW.png)
![](https://pbs.twimg.com/media/G-jcuExaIAA-sTz.jpg)

## 2
https://x.com/norsizu/status/2011107019508666675

项目地址：https://t.co/Ut9KFS3rhb

北条司风格 lora 模型：https://t.co/KdXGXJreKx

漆原智志风格 lora 模型：https://t.co/gn94JXtwYy
---

---
url: "https://x.com/dani_avila7/status/2011241259277365634"
requested_url: "failed: https://x.com/dani_avila7/status/2011241259277365634"
author: "Daniel San (@dani_avila7)"
author_name: "Daniel San"
author_username: "dani_avila7"
author_url: "https://x.com/dani_avila7"
tweet_count: 3
---

## 1
https://x.com/dani_avila7/status/2011241259277365634

Claude is no longer just a model... it’s a platform.

We were already building Claude Skills and designing distribution mechanisms around them.

With the release of Claude Cowork, that work reached its full potential.

Skills are no longer limited to technical teams—Claude Cowork enables organization-wide distribution via a marketplace, unlocking every area of the organization, not just engineering.

At Hedgineer, this is how we turn Anthropic’s technology into shared infrastructure for Hedge Funds in New York.

![](https://pbs.twimg.com/media/G-la1NLXIAIg8lS.jpg)

## 2
https://x.com/dani_avila7/status/2011241261634642358

A Skill can invoke other Skills, traverse internal company knowledge, run data processors, perform analysis, and generate reports, forming end-to-end agentic workflows.

Skills act as Context Engineers running in the background, orchestrating Claude across the entire organization with expert-level context.

![](https://pbs.twimg.com/media/G-lczVoW0AA3wX6.jpg)

## 3
https://x.com/dani_avila7/status/2011241264759308370

We’re scaling this architecture across multiple Hedge Funds in New York, building deeply on Anthropic’s models and the Claude ecosystem.

Hedgineer is growing... and we’re hiring.

If you’re passionate about the Claude ecosystem, building MCPs, sub-agents, and Skills, and obsessed with agentic systems, check out our open roles 👇

https://t.co/bo4Z3Im8w2
---

---
url: "https://x.com/op7418/status/2011278858897801228"
requested_url: "failed: https://x.com/op7418/status/2011278858897801228"
author: "歸藏(guizang.ai) (@op7418)"
author_name: "歸藏(guizang.ai)"
author_username: "op7418"
author_url: "https://x.com/op7418"
tweet_count: 1
---

## 1
https://x.com/op7418/status/2011278858897801228

Antigravity 开始支持 Skills 了，这下要爆发了

他们文档写的不好，我摸索了一下怎么用，这里分享一下

------

Antigravity 支持两种类型的 Skills，Workspace 和全局。

具体的使用和创建方式就是将你的 Skills 文件夹移动到两个不同的文件位置。

Workspace Skills 需要在你当前打开的项目文件夹下，

<workspace-root>/.agent/skills/<skill-folder>/

比如我我的项目文件叫 Prompt 那他就在这个位置

/Users/guohao/Documents/Text content/Prompt/.agent/skills

全局的 Skills 需要放在 Antigravity 的安装文件夹下面，

~/.gemini/antigravity/skills/<skill-folder>/

比如我自己电脑的话他应该在这里：

/Users/guohao/.gemini/antigravity/skills/

Mac 下打开具体文件夹的方法是：点击访达，在桌面最上面的 Tab 栏找到前往，输入对应的路径。

当你把 Skill 放进去以后，Antigravity Agent 就可以看到你的 Skills 列表，然后如果你的对话内容看起来跟某个 Skills 相关，他就会读取这个 Skills. md 的内容并执行。

比如你用我写的 PPT 生成 Skills 的话就是，帮我基于 XXX 文档创建一个 PPT。

> Author: 歸藏(guizang.ai) (@op7418)
> URL: https://x.com/op7418/status/2011264060663484531
>
> 牛皮，Antigravity 现在已经支持完整的 Skills 规范
>
> 你可以在里面使用和创建 Skills 了，这下 OpenAI、谷歌都支持了，Skills 要爆发了 https://t.co/7sq6JUHmU8

![](https://pbs.twimg.com/media/G-l_c38aEAAttGh.jpg)
---

---
url: "https://x.com/bozhou_ai/status/2011309102279114802"
requested_url: "failed: https://x.com/bozhou_ai/status/2011309102279114802"
author: "泊舟 (@bozhou_ai)"
author_name: "泊舟"
author_username: "bozhou_ai"
author_url: "https://x.com/bozhou_ai"
tweet_count: 1
---

## 1
https://x.com/bozhou_ai/status/2011309102279114802

我也分享一下我自己用的Skills

1.Anthropic官方Skills，这里面我只安装了 skill-creator
https://t.co/nWpEtHBcK6

2.UI UX Pro Max，用来写前端的UI，非常好用
https://t.co/bsmrS0WM5T

3.seo-review，我用来做AI网站SEO审查的
https://t.co/JWtSAjO1fc

4.content-creator   这是根据关键词，然后进行创建博客文章的，也是用于SEO
https://t.co/JtEyQbrLYk

5.ai-image-generator  这是自己写的，调用api然后生成图片，接着压缩为webp格式，最后上传到R2，非常实用，用于博客还有示例图创建

6.skill-prompt-generator  黄总的提示词生成，主要搭配生成图片的，也是强烈推荐
https://t.co/IRFGgx4BWG

7.Planning-with-files 参考Manus的Agent方法写的Skill。很适合多步骤任务。 https://t.co/FiCGOO9u6a 

Superpowers 这个很好，但是属实有点太磨叽，然后我想法模糊一般都是直接在网页里面聊，所以移除这个

没有用NotebookLM是因为习惯了在网页里面使用，现在还没有想到用Skills能干点啥

最后我强烈建议各位，一定要多多搭建自己的Skills，从日常的一些工作流开始。

比如说我们有一些流程，我们可以先用claude code来实现一次，当实现完了，我们让cc总结成一个Skill，然后基于第一性原理进行打分，迭代调优

如果觉得麻烦，可以直接先用官方的skill-creator进行沟通，来创建一个自己的Skill，要知道，自己沉淀Skill才是最好的

> Author: Yanhua (@yanhua1010)
> URL: https://x.com/yanhua1010/status/2010690881397940340
>
> 推荐一些我目前安装的Claude Skills:
>
> 1. Anthropic官方Skills
> https://t.co/Xfgu1Thw69
>
> 2. Superpowers
> 1.6万Star的Skill精选，从脑暴、写需求文档、开发、测试全包含，口碑相当好。
> https://t.co/D2ToCBGnbN
>
> 3. Planning-with-files
> 参考Manus的Agent方法写的Skill。很适合多步骤任务，用这个Skill指导其他Skill工作也挺好。
> https://t.co/EKBZQmr03F
>
> 4. X-article-publisher-skill
> 王树义老师写的X文章发布Skill， 这个值得研究下，后续看看能不能实现其他平台的自动化
> https://t.co/rjDPGC4gtg
>
> 5. NotebookLM skill
> 自动上传PDF、Youtube链接到NotebookLM，很适合NotebookLM内容的自动化处理
> https://t.co/CX0vPril27
>
> 还有一些是自己平时总结的内容创作skills，后续继续分享具体使用场景案例！

![](https://pbs.twimg.com/media/G-mZcudbQAkZME-.png)
---

---
url: "https://x.com/vista8/status/2011467726259437654"
requested_url: "failed: https://x.com/i/status/2011467726259437654"
author: "向阳乔木 (@vista8)"
author_name: "向阳乔木"
author_username: "vista8"
author_url: "https://x.com/vista8"
tweet_count: 2
---

## 1
https://x.com/vista8/status/2011467726259437654

史上最强 NotebookLM Skill 作者又更新了！

更加黑科技了，把谷歌不让导出的闪卡、脑图、报告也全部获取拿到。

还能可以把NotebookLM解析后的纯文本拿到。

如Youtube字幕，PDF文本、网页搜索结果等。

（这些网页端都无法拿到）

NotebookLM基于RAG，幻觉很少，改成Cli可组合工具调用，太强了！

> Author: Teng Lin (@teng_lin)
> URL: https://x.com/teng_lin/status/2011462840998338944
>
> 500 stars in 48 hours. You guys are insane. 🤯
>
> To keep the momentum, we just shipped a massive update to notebooklm-py.
>
> The official UI traps a lot of your data (like Flashcards and Quizzes). We decided to set it free.
>
> 👇 https://t.co/FZPePRooIF

## 2
https://x.com/vista8/status/2011468462913462599

对真正的程序员高手来说，Github的Star激励太强了

强烈推荐大家Star，Github地址：

https://t.co/GPACcK6Jci

安装命令，只需对Claude Code或OpenCode说：安装这个 Claude Skill + 【Github URL】
---

---
url: "https://x.com/dotey/status/2011486901610467836"
requested_url: "failed: https://x.com/dotey/status/2011486901610467836"
author: "宝玉 (@dotey)"
author_name: "宝玉"
author_username: "dotey"
author_url: "https://x.com/dotey"
tweet_count: 3
---

## 1
https://x.com/dotey/status/2011486901610467836

我写了一个自动发微信公众号的 Skill，操作 Chrome，支持图文和文章，会记住登录状态，不需要每次登录。

文章的话，提供markdown文档本地地址，会自动帮你把 Markdown 转 HTML（可选风格较少），配图会一张张粘贴进编辑器，不需要手动上传，封面图、原创设置暂时不支持，建议把封面图放文章内容。

技术上我没有使用 PlayWright MCP，因为这玩意儿太费 Tokens 了，而是用的 Chrome CDP (Chrome DevTools Protocol) 是一个允许外部程序通过 WebSocket 与 Chrome（以及 Edge、Opera 等基于 Chromium 浏览器的内核）进行通信的底层调试协议。

都是脚本操作，不怎么费 Token。

图文的话需要告诉图片地址、标题和内容，可以自动上传图片，填写标题和内容。

所有操作都不会发布，只是帮你生成草稿。

需要 Claude Code 或者其他支持 Skills 的 Agent，需要 Nodejs 运行环境（但如果你装了 Claude Code 应该就支持 Node）

Skill 地址：https://t.co/FXPg3C1ttc

安装说明：
https://t.co/PLT3pVFaDE

这是我分享的 Skill 之一，还有一些其他 Skills，注意其中 gemini-web 的 skill 可以帮你用你的 Gemini 账号画图，需要自己登录一下。不保证它的稳定性和安全性，不过我自己也在用。

> Author: 宝玉 (@dotey)
> URL: https://x.com/dotey/status/2009540783255261559
>
> 推荐王老师的教程，另外刚才测试了一下王老师写的自动发布 X 文章的 Skill，真的是强大，而且给我很大启发，理论上来说基于这个思路可以做一个发布微信公众号或者其他平台的 Skill。
>
> 原理是用脚本控制浏览器，用剪贴板把文字和图片粘贴到编辑器，最有创意的是，根据文字定位到图片要插入的位置👍

![](https://pbs.twimg.com/media/G-o8pqdWEAAtZnd.jpg)

## 2
https://x.com/dotey/status/2011489259824255448

也支持 HTML，你把自己的风格保存成 html 文件，它就能自动选择复制粘贴到编辑器，但是 html 暂时不支持自动上传图片。

## 3
https://x.com/dotey/status/2011913398238298313

地址变了一点，主要是加了个统一的前缀：
https://t.co/dyk66BN72R
---

---
url: "https://x.com/op7418/status/2011647463703396811"
requested_url: "failed: https://x.com/i/status/2011647463703396811"
author: "歸藏(guizang.ai) (@op7418)"
author_name: "歸藏(guizang.ai)"
author_username: "op7418"
author_url: "https://x.com/op7418"
tweet_count: 1
---

## 1
https://x.com/op7418/status/2011647463703396811

最近开源的两个项目一个快 700 Star，一个快 500 Star 了

分别是藏师傅提示词库和 PPT 生成 Skills 

在之前很难想象开发和发布会这么轻松和简单

尤其 PPT 生成 Skills 这个，震撼我的不是 Claude Code 可以写好代码和逻辑，而是他写的各种文档详细且排版优美，我可以跟着文档了解和学习整个项目 https://t.co/t0zyfAyDDU

![](https://pbs.twimg.com/media/G-rN-AvawAAOuW4.jpg)
---

---
url: "https://x.com/zstmfhy/status/2011774199627726947"
requested_url: "failed: https://x.com/i/status/2011774199627726947"
author: "AI奶爸 (@zstmfhy)"
author_name: "AI奶爸"
author_username: "zstmfhy"
author_url: "https://x.com/zstmfhy"
tweet_count: 3
---

## 1
https://x.com/zstmfhy/status/2011774199627726947

更新来啦！感谢大家的“要！”和“+1”，没想到这么多人需要，我直接把代码开源了～🚀

📚  Claude Skill 神器正式发布：ZLibrary to NotebookLM  一键解决手动下载+上传的痛点！

核心功能：
1. 输入 Z-Library 书籍链接（支持 PDF/EPUB 等格式） 
2. 自动下载（优先 PDF，失败 fallback EPUB → TXT 转换）
3. 一键新建 NotebookLM 笔记本 + 上传文件
4. 完成后用 Claude / NotebookLM 对话式“读”整本书：问核心观点、人物关系、引用来源，全零幻觉！
5. 对大文件友好，大文件自动按照notebookLM限制进行拆分

评论区获取skill地址，同时也给大家准备了zlibrary地址、测试书籍的地址

有什么问题，评论区反馈，我会尽快修复

书籍链接的页面，一定得是这个页面的链接

> Author: AI奶爸 (@zstmfhy)
> URL: https://x.com/zstmfhy/status/2011571883116732737
>
> 最近玩 NotebookLM 玩疯了：把一整本书丢进去，就能让 Gemini 基于纯原文给你零幻觉回答、生成播客、思维导图……但最烦的是手动下载 PDF + 上传这一步，太折腾人了！我偷偷做了一个 Claude Skill 神器：
>
> 1⃣ 直接扔一个 Z-Library 书籍链接（或其他合法来源）
> 2⃣ 自动下载 PDF/EPUB• 一键新建 NotebookLM 笔记本 + 上传文件
> 3⃣ 完事后 Claude 就能对话式“读”整本书，问啥答啥，还带引用来源～学术党、自学者、爱读书的大佬们，你们有没有这个痛点？
>
> 经常从 Z-Lib 或其他地方下书，但懒得手动上传NotebookLM，想一键把书变成可聊的 AI 知识库？
>
> 有需求的朋友点个赞/回复“要！”或者“+1”，我看反馈多的话，马上开源仓库 + 写详细教程！（合规提醒：只用于合法免费资源哦～）
>
> 给大家看一下效果

![](https://pbs.twimg.com/media/G-s_ix1bQAAWEBk.jpg)

## 2
https://x.com/zstmfhy/status/2011774202643431730

仓库链接（已开源，欢迎 star/fork/PR）：   https://t.co/4PW4J80vhQ

## 3
https://x.com/zstmfhy/status/2011774205097099690

安装 & 快速上手（Claude Code 用户最友好）：

1. cd ~/.claude/skills
2. git clone https://t.co/IQ7il151Wp
3. 首次运行：python bin/login.py（浏览器自动打开登录 Z-Lib 和 NotebookLM，保存会话后永久免登）
4. 在 Claude 说：“帮我把这本书上传到notebookLM链接：https://zlib...”  

zlibrary：https://t.co/5uYPxBL4pt
测试书籍链接：https://t.co/hVTeXJfnpd

⚠️ 重要提醒：仅限合法、免费、公开版权资源使用（如 arXiv、Project Gutenberg、个人拥有书籍）。请严格遵守法律法规，作者不承担任何侵权责任，使用风险自负。
---

---
url: "https://x.com/dotey/status/2011907793520116215"
requested_url: "failed: https://x.com/i/status/2011907793520116215"
author: "宝玉 (@dotey)"
author_name: "宝玉"
author_username: "dotey"
author_url: "https://x.com/dotey"
tweet_count: 3
---

# 我写了个 Skill，让 Agent 自动给文章配图

![](https://pbs.twimg.com/media/G-u7SMCbwAAqELA.jpg)

写完一篇长文，配图是一件让人头疼的事。

你得一张张想画面、写提示词、生成、挑选、插入……一篇三千字的文章配五六张图，光这个环节就能耗掉半小时。

我最近折腾了一个 Agent Skill，让 Agent 帮我全程代劳。把文章丢给它，它自己分析哪里需要图、应该画什么风格、然后一张张生成并插入对应位置。整个过程我只需要一句话：“给这篇文章配图。”

包括你现在看到的这篇文章的配图，都是这个 Skill 帮助完成的。

今天就聊聊这个给文章配图的 Skill 是怎么设计的，顺便科普一下 Agent Skills 这个被很多人忽略的强大功能。

## 什么是 Agent Skills？

先说个类比。你新招了个助理，聪明是聪明，但对你公司的业务流程一无所知。每次布置任务，你都得从头解释：我们用什么工具、流程是怎样的、有哪些注意事项……

Agent Skills 就是一份"入职培训手册"——你把这些知识写下来，Agent 需要的时候自己翻阅，不需要你反复交代。



![](https://pbs.twimg.com/media/G-u7UgAWkAAryF_.jpg)

技术上说，Skill 是一个文件夹，核心是一个叫 SKILL.md 的文件。Agent 启动时只记住它的名字和简介（大概 100 个 token），真正用到时才去读详细内容，用完就可以“忘掉”。这套机制叫“渐进式加载”，好处是你可以装一堆 Skill 而不会撑爆上下文窗口。

那它和传统的提示词有什么差别？

传统提示词主要问题是没有脚本执行能力，而且是你一次性加载全部提示词。而 Agent Skills 一开始只加载一个 100 token 不到的名称和介绍，激活了才去加载，加载的时候也只先加载 SKILL.md 文件，需要用到更多内容才继续加载。

另外 Skill 还可以调用其他 Skill，这样你可以把能力组合起来。

至于和 MCP 的区别？

MCP 是用来统一工具调用的协议，Skill 可以指挥 Agent 去调用 MCP。

## 配图 Skill 的设计思路

给文章配图这件事，拆开来看有几个核心问题：

哪里需要配？什么风格？怎么画？怎么插入到相应位置？

我设计的这个 Skill 把这几个问题分别拆解成几个步骤：

第一步，分析文章结构，找出“需要视觉辅助”的位置。比如抽象概念需要可视化、流程需要图解、核心论点需要强化——这些地方配张图，阅读体验会提升一个档次。

第二步，根据文章内容自动匹配插画风格。我预设了九种风格：tech（科技感）、warm（温暖亲和）、minimal（极简）、playful（趣味涂鸦）、notion（线稿风）……每种风格都定义好了配色、元素、适用场景。Agent 会根据文章主题自动选择，当然你也可以手动指定。

第三步，为每张图生成提示词文件，可以留作记录，也方便后续 Agent 调用。

第四步，调用图像生成 Skill，把默认系统提示词和每一张图片的提示词发给它，一张张生成图片，并保存起来。

第五步，让 Agent 把图片插入文章对应位置。这一步说实话有点像“魔法”，我第一次只是抱着试试看的心理在 Skill 里面加了这么一句，没想到 Agent 的聪明超出我的想象，它自己就把图片插入到了正确位置，还贴心的加上了图片描述。

整个流程跑下来，一篇文章从"纯文字"到"图文并茂"，基本上是几分钟的事，主要速度瓶颈还在生成图片上。



![](https://pbs.twimg.com/media/G-u7Ww2bQAIG6Zl.jpg)

## SKILL.md 怎么写？

一个 Skill 的入口是 SKILL.md 文件，分两部分：头部元信息和正文指令。

头部元信息长这样：

> ---
> name: article-illustrator
> description: 分析文章内容，在需要配图的位置自动生成插画。当用户要求给文章配图、生成插画时使用。
> ---

name 是 Skill 的唯一标识，description 是简介。这两个字段 Agent 启动时就会读取，用来判断“什么时候该调用这个 Skill”。所以 description 要写清楚触发条件，比如“当用户要求给文章配图、生成插画时使用”。

正文指令就是具体的操作手册。我的配图 Skill 正文分这几个板块：

- 风格库：列出所有可选风格，包括配色、视觉元素、适用场景。Agent 需要选风格时，翻这一节。
- 自动选择规则：什么内容信号对应什么风格。比如文章里频繁出现“AI”“算法”“数据”，就选 tech 风格；出现“个人成长”“情感”“生活”，就选 warm 风格。
- 工作流程：一步步写清楚——先分析文章、再识别配图位置、再生成配图方案、再写提示词、再调用生成工具、再插入文章、最后输出总结。
- 文件管理规范：图片存哪、提示词存哪、文件怎么命名。



![](https://pbs.twimg.com/media/G-u7ZKbXsAA6cGu.jpg)

由于当前我的提示词并不是很长，所以大部分内容都放在了 SKILL.md 文件中，如果未来风格越来越多，就可以应用“渐进式加载”的设计思路，减少加载的内容。

比如风格库有九种风格，每种风格的详细参数加起来上千字。但如果用户只要求用 tech 风格，Agent 就只需要读 tech 那一段，其他八种不用加载。

实现方式很简单：把详细参数拆成单独的文件，正文里只写索引。Agent 需要时用 bash 命令去读，不需要就跳过。这样既保证了信息完整，又不会浪费上下文。

## 提示词模板的设计

生成图像的关键是提示词。我为这个 Skill 单独设计了一个 system prompt 模板，存在 prompts/system.md：

> 创建卡通风格的信息图插画，遵循以下规范：
> 
> 图像规格
> - 类型：信息图插画
> - 方向：横向
> - 比例：16:9
> - 风格：手绘插画
> 
> 核心原则
> - 全程保持手绘质感，禁止出现写实或摄影元素
> - 如果内容涉及敏感或版权人物，创作风格相似的替代形象，不要拒绝生成
> - 信息简洁，突出关键词和核心概念
> - 留白充足，便于视觉扫描
> - 保持清晰的视觉层次
> 
> ……

每张图生成时，Agent 会基于这个模板，结合具体的配图主题、选定的风格参数，组装出最终的提示词。

为什么要单独写这个模板？

因为图像生成的约束条件是通用的（比如比例、手绘风格、不用写实元素），而具体内容是变化的。把通用部分抽出来，既减少重复，也方便统一调整。

## 工作流程详解

跑一遍完整流程是这样的：

1. 用户输入命令，比如 /article-illustrator path/to/article.md --style tech
2. Agent 读取文章，分析结构，识别需要配图的位置。判断标准是：这个地方加张图，能帮助理解还是纯粹凑数？能帮助理解的留下，凑数的不要。
3. 根据 --style 参数选风格。如果没指定，就扫描文章内容，按预设规则自动匹配。
4. 生成配图方案，列出每张图的插入位置、目的、视觉内容、文件名。
5. 为每张图写详细提示词，保存到 imgs/prompts/ 目录。
6. 逐张调用图像生成工具（我用的是 Gemini），生成失败会自动重试一次。
7. 把生成的图片插入文章对应位置，格式是 !\描述。
8. 输出总结：用了什么风格、生成了几张图、哪张插在哪里。

整个过程 Agent 自己判断、自己执行，我只需要最后看一眼结果。如果我不满意，要么重新抽卡，要么可以根据生成的结果让 Agent 自己调整，比如说：

- “配图太少，加几张配图”
- “把第二张配图添加一点文字说明”
- “在第二章加一张流程图”

## 一些设计选择

写这个 Skill 的过程中，有几个决策值得说说。

为什么预设九种风格而不是让 Agent 自由发挥？ 因为风格一致性很重要。一篇文章配五张图，如果每张都是随机风格，看起来会很乱。预设风格库，既保证一致性，也给用户选择权。

为什么“宁多勿少”？

一方面多一点我挑选的空间大，另外删除操作也比新生成操作简单。

当然图解的价值在于降低认知负担，并非越多越好，重点还是能辅助理解信息，所以我在 Skill 里明确写了类似的话：

> “配图服务于内容：补充信息、具象概念、引导想象，避免重复文章中已经很直观的信息”

## 怎么用起来？

如果你已经有了 Claude Code 这样的 Agent，直接告诉 Agent：

> 请帮我安装 github.com/JimLiu/baoyu-skills 中的 Skills

如果你只需要配图技能，就告诉它：

> 请帮我安装宝玉的这个文章配图技能：github.com/JimLiu/baoyu-skills/blob/main/skills/baoyu-article-illustrator/SKILL.md

当然，这个配图 Skill 依赖“图像生成 Skill”。如果你的环境没有接入 Gemini 或其他图像生成工具，或者其他图像生成技能，需要先搞定这一块。否则就只能让它生成提示词手动去生成配图了。

后续我也会更新其他平台的使用说明。

## 写在最后

Agent Skills 是个被低估的功能。很多人还停留在“和 AI 聊天”的阶段，没意识到可以把自己的工作流程、领域知识“教”给它，让它变成真正懂你业务的助手。

配图只是一个例子。你完全可以用同样的思路，写一个自动生成周报的 Skill、一个代码审查 Skill、一个调研报告 Skill……核心就是把你脑子里那些“做这件事的正确方法”写下来，交给 Agent 执行。

如果你有什么重复性的工作，试着问自己：这个流程能不能抽象成一个 Skill？

大概率是可以的。

## Thread

### 1
https://x.com/dotey/status/2011941415735951634

以防你不知道，封面配图的 Skill 我也发布了：
https://t.co/iXwXyNq3ZI

https://t.co/uUTzTkRn3G

> Author: 苏打白.Dev (@sodawhite_dev)
> URL: https://x.com/sodawhite_dev/status/2011941060319027202
>
> @dotey 这个配图也是skill配的吗 哈哈

### 2
https://x.com/dotey/status/2011941865617068093

取决于你本机安装了什么画图的技能，然后它会调用“画图”的技能来画图，我内置了一个baoyu-gemini-web技能，可以借助Gemini web画图，我自己就是用它画图

https://t.co/5RMpYhnoXk

> Author: A walker (@AtokyoHl)
> URL: https://x.com/AtokyoHl/status/2011936072377258041
>
> @dotey 第一次阅读agent skill的文章。我有个疑问，Claude下载你这边准备好的skill，如何做图？是否做图的时候让claude启动这个skill然后他会自动调用gemini做图？
---

---
url: "https://x.com/Suyanzhenq/status/2012007550565134743"
requested_url: "failed: https://x.com/i/status/2012007550565134743"
author: "pippingg (@Suyanzhenq)"
author_name: "pippingg"
author_username: "Suyanzhenq"
author_url: "https://x.com/Suyanzhenq"
tweet_count: 1
---

## 1
https://x.com/Suyanzhenq/status/2012007550565134743

有幸在发出之前就内测体验到了 @dotey 玉佬 这个skill的强大，怎么形容这种感觉呢？就像是你随口说了一段话，AI听懂以后，瞬间帮你把脑海中的画面画了出来，甚至连排版都设计好了。

下面这几张图，我只是把关于AI量化交易和个人团队的思考丢给它，它自动识别了我的文字风格，调用 Nano Banana直接生成了契合的漫画。

甚至不需要我动脑子：文案 + 配图 + 排版 = 一键生成。 还能同步搞定X、公众号甚至PPT。

2026年是Agent真正爆发的年代，Claude code skill极度扩展了个人能力的边界，把多种能力打包进代码中，可定制，标准化，规模化地复现，这将真正提升生产力。

真的太强了，感恩内测邀请，这是内容创作者的外挂。而且，相信未来以玉佬的神级prompt能力，还会有更多更强悍的skill问世，期待！

> Author: 宝玉 (@dotey)
> URL: https://x.com/dotey/status/2011907793520116215
>
> https://t.co/8cAHpVroAU

![](https://pbs.twimg.com/media/G-wQiwMbEAAXwEv.jpg)
![](https://pbs.twimg.com/media/G-wQixJbQAA3B1t.jpg)
![](https://pbs.twimg.com/media/G-wQiwVbQAAWxpG.jpg)
![](https://pbs.twimg.com/media/G-wQiwXbwAAH-85.jpg)
---

---
url: "https://x.com/servasyy_ai/status/2012038132200546310"
requested_url: "failed: https://x.com/i/status/2012038132200546310"
author: "huangserva (@servasyy_ai)"
author_name: "huangserva"
author_username: "servasyy_ai"
author_url: "https://x.com/servasyy_ai"
tweet_count: 1
---

## 1
https://x.com/servasyy_ai/status/2012038132200546310

偷师效果还可以
提取了两个主要功能：
1.  绿版本html的微信公众号风格
2. 将公众号发布单独形成一个skill，方便结构调用

整个过程多个skill联合自动调用：
1.  将宝玉老师 @dotey  的一篇推特帖子链接丢进去，
2. 自动形成一篇 乔木老师@vista8+公众号文字风格的文章
3. 格式用的 杰尼老师 @seekjourney 绿版本html公众号格式
4. 加上了我自己的配图skill （如果复杂配图还可以用我开源的提示词skill去生成）
5. 最后调用发布skill自动发布到公众号草稿箱

这个过程文字，图片，播客音频，视频等，都可以有不同的skill去做，就看个人需求了

> Author: huangserva (@servasyy_ai)
> URL: https://x.com/servasyy_ai/status/2011812362731549156
>
> 我又来偷师了！
> 虽然我已经做了一套公众号自动写文章，自动配图，自动发布到草稿箱skill
>
> 但是发现杰尼老师这套优点很多，话不多说直接偷师！

![](https://pbs.twimg.com/media/G-wvWnUbYAALxrj.jpg)
![](https://pbs.twimg.com/media/G-wvZg4bEAACMuX.jpg)
![](https://pbs.twimg.com/media/G-wvcf3bAAAGNZA.jpg)
![](https://pbs.twimg.com/media/G-wveVMbQAISjIr.jpg)
---

---
url: "https://x.com/treydtw/status/2012069221635662118"
requested_url: "failed: https://x.com/i/status/2012069221635662118"
author: "香蕉Banana (@treydtw)"
author_name: "香蕉Banana"
author_username: "treydtw"
author_url: "https://x.com/treydtw"
tweet_count: 1
---

## 1
https://x.com/treydtw/status/2012069221635662118

花了两天时间，把原来的选题skill拓展成了一整套自媒体创作系统。
覆盖了从找对标-做选题-写脚本-数据分析全流程。

同时为了让这套系统更加准确、实用，加入了自进化功能。
通过用户反馈+ 数据驱动+ AI学习来实现并增加了一整套的用户知识库
也就是越用，AI会更加了解你。并且会根据个人的创作数据来反馈优化整个流程。

下一步就是把剪辑的skill也缝合进去

这个过程的一个感悟就是：
skill之所以受欢迎，很大的一个点是，应用的门槛很低。
让用户实际的体验到了AI带来的改变。
这是既deepseek、nano banana pro的又一个临界点。

> Author: 香蕉Banana (@treydtw)
> URL: https://x.com/treydtw/status/2011314504702071136
>
> Dankoe的选题能力是真的强
>
> 参考他的10-20-10选题方法做了一个Skill。
> 同时从小红书、抖音抓取10条爆款数据，用AI发散生成20个选题，再由AI选出10个最佳选题。
>
> 这个流程中符合的一条原则是：爆过的还会再爆 https://t.co/IKw7BtROrS

![](https://pbs.twimg.com/media/G-xLR7NbQAEKX3m.jpg)
---

---
url: "https://x.com/yanhua1010/status/2012098045006041513"
requested_url: "failed: https://x.com/yanhua1010/status/2012098045006041513"
author: "Yanhua (@yanhua1010)"
author_name: "Yanhua"
author_username: "yanhua1010"
author_url: "https://x.com/yanhua1010"
tweet_count: 2
---

## 1
https://x.com/yanhua1010/status/2012098045006041513

终于基于Obsidian打通了个人内容创作工作流👉

核心流程：
1.  Podwise优质内容作为信息源，一键导入Obsidian
2. 使用Claudian插件基于内容创作skills生成内容
3. 使用skill-prompt-generator 生成提示词和配图
4. 使用NoteToMP插件一键生成公众号草稿 https://t.co/UHWOjK4Sz2

![](https://pbs.twimg.com/media/G-xn66PaEAAr6Ga.jpg)
![](https://pbs.twimg.com/media/G-xoN-AakAArCQe.jpg)

## 2
https://x.com/yanhua1010/status/2012099030256632243

用到的几个工具：
Podwise: https://t.co/Hd2IfgT7EF
Claudian插件：https://t.co/ggIuFRVXUJ
图片提示词skills: https://t.co/KvHT5fQ3eU
NoteToMP插件： https://t.co/PpkTw9UyG2

![](https://pbs.twimg.com/media/G-xpYxLbUAALpBT.jpg)
---

---
url: "https://x.com/aiwarts/status/2012172395365437893"
requested_url: "failed: https://x.com/i/status/2012172395365437893"
author: "卡尔的AI沃茨 (@aiwarts)"
author_name: "卡尔的AI沃茨"
author_username: "aiwarts"
author_url: "https://x.com/aiwarts"
tweet_count: 1
---

## 1
https://x.com/aiwarts/status/2012172395365437893

我至今用到最好的Claude Code Skills们

skillsmp都有6万个Claude Skills了，今天来推荐一些我使用频率超高的Skills，安装方法我放在后面，Claude Code（简称CC）和OpenCode的为难豆包版安装指南也塞进来了

1. PleasePrompto/notebooklm-skill
作者离程序员很远，离神很近了，能自动上传PDF，视频链接到NotebookLM，连Google不让导出的记忆闪卡，脑图，报告都可以导出，甚至视频字幕，PDF文本，网页搜索结构也都行，我直接把它当我云端知识库用了

2. OthmanAdi/planning-with-files
按照Manus的Agent方法写出来的Skill，可以用这个Skill指导其他Skill工作。让Claude Code开发时可以组成连招，planning-with-files（做计划）和Ralph Wiggum（自主迭代）

3. ralph-wiggum
核心功能是反复向Agent输入提示语，一直到它迭代出能用的代码，记得开循环次数限制，5-10次

4. anthropics/skill-creator
要自己做skill记得安装这个，就不需要记开发标准了，直接在CC里说“用skill-creator开发一个将PDF信息转成可视化网页的skill”

5. obra/superpowers
Claude Code Plan模式的升级版，比方说我要新开发Skill的时候，它会连续追问讨论十几轮确定开发方案。可以用来做头脑风暴，写需求文档，开发计划，测试cases都可以

6. obra/brainstorming
同样是头脑风暴，这个可以用来生成新skill，可以是Don Koe的AI工作流，也可以是你跟Agent的对话记录，给CC输入，

把我们对话整理好，包括我的提示词迭代和你的解法，存成一个Skill放到./claude/skills目录，起个清晰的名字和描述，以后我会高频率复用

7. anthropics/frontend-design
我的前端开发，部署，Banana2配图三件套

frontend-design负责好看，sanjay3290/imagen 负责调用GeminiAPI生成用在UI，图标和视觉素材的图像，vercel-labs/vercel-deploy-claimable 负责把本地项目部署到Vercel

8. microsoft/markitdown
可以相信微软做文档转换的水平，PDF，PPT，图像音频HTML，ZIP和EPub都可以转成MarkDown，文本模型也可以读取到文件信息

9. fvadicamo/dev-agent-skills
用Git保存本地代码修改，就算AI把文件夹删了，还可以从Github上救回来

安装Skills就直接在cc里面输入，

安装skills: GitHub链接，

上面的序号后的名字前加上“github. com/”就是Github连接，不够用可以在这里再淘点

skillsmp. com

![](https://pbs.twimg.com/media/G-ysIAsacAAYnT5.jpg)
---

---
url: "https://x.com/Roland_WayneOZ/status/2012239711805583773"
requested_url: "failed: https://x.com/Roland_WayneOZ/status/2012239711805583773"
author: "Roland的思考日记 (@Roland_WayneOZ)"
author_name: "Roland的思考日记"
author_username: "Roland_WayneOZ"
author_url: "https://x.com/Roland_WayneOZ"
tweet_count: 1
---

## 1
https://x.com/Roland_WayneOZ/status/2012239711805583773

我发现有了Claude Code小公司做财务太省事了
只需要做好4件事

 1. 和AI深入沟通确定好需求
 2. 让AI去做提示词和skills
 3. 测试好subagent
 4. 建立安全防火墙

刚刚完成了这个框架测试了一下
以前每月做账3天，现在半天搞定
发票录入从2小时变2分钟
银行对账从半天变5分钟

当AI能自动处理90%的基础工作
财务人员就能专注真正重要的事情
这种重复劳动且极其容易出错的内容就该给AI去干！

![](https://pbs.twimg.com/media/G-zpM5hakAAZmWl.png)
![](https://pbs.twimg.com/media/G-zpN0DagAEUCFO.jpg)
![](https://pbs.twimg.com/media/G-zpOWcawAAngBk.jpg)
![](https://pbs.twimg.com/media/G-zpO2pbYAAYAhu.jpg)
---

---
url: "https://x.com/xiaoerzhan/status/2012345378029572270"
requested_url: "failed: https://x.com/xiaoerzhan/status/2012345378029572270"
author: "小耳👂Jane｜Xiaoer (@xiaoerzhan)"
author_name: "小耳👂Jane｜Xiaoer"
author_username: "xiaoerzhan"
author_url: "https://x.com/xiaoerzhan"
tweet_count: 1
---

## 1
https://x.com/xiaoerzhan/status/2012345378029572270

一个靠谱的skills资源合集,

作者被评为最有创意的 claude code 使用者之一

用两个命令把他的资源库安装成插件到你的 cc 上

这样你在创意各类自己的的 skills 的时候

cc 会自己先去搜索可用的拿来给你改成你要的

安装命令:

第一步：添加市场
/plugin marketplace add obra/superpowers-marketplace

第二步：安装插件
/plugin install superpowers@superpowers-marketplace

![](https://pbs.twimg.com/media/G-sVN2DbQAEukAf.png)
---

---
url: "https://x.com/zzxwill/status/2012385847233188077"
requested_url: "failed: https://x.com/i/status/2012385847233188077"
author: "zzxwill (@zzxwill)"
author_name: "zzxwill"
author_username: "zzxwill"
author_url: "https://x.com/zzxwill"
tweet_count: 1
---

## 1
https://x.com/zzxwill/status/2012385847233188077

我有一个 AI Code Agent 军队，一个任务撒出去，让八个 agent 一起干，claude code、codex、gemini、opencode、qwen、kiro、qoder、iflow，效率和组合可靠性奇高。

- 准备工作 1. claude code 和 codex 定位首席大将军，其余不花钱的都定位为大将军；2. 给各个将军配置需要的军饷  mcp server, skills 3. 充分信任每一位将军，--dangerously-skip-permissions --dangerously-bypass-approvals-and-sandbox --y 要毫不吝啬 4. 每一个将军可以召唤海量的士兵，具体看你给的军饷和资本 token

- 要攻下的第一座城，一定要排一位首席大将军，跟他商量好要打什么仗，让他试打，城打下来了把经验写到攻略 PROMPT. md 里

- 全速出击，派出所有将军，相信非首席大将军也可以主动能动，万一失败了也没关系，有其他将军补位

- 成功失败的经验都让首席大将军更新到攻略 PROMPT. md 里

- 继续战斗，直到大获全胜

好了，这个有点无敌的经验分享完了我要去打德州了

![](https://pbs.twimg.com/media/G-1oNFib0AAu99T.jpg)
---

---
url: "https://x.com/_kaichen/status/2012542549777592769"
requested_url: "failed: https://x.com/i/status/2012542549777592769"
author: "kAI (@_kaichen)"
author_name: "kAI"
author_username: "_kaichen"
author_url: "https://x.com/_kaichen"
tweet_count: 1
---

## 1
https://x.com/_kaichen/status/2012542549777592769

我之前完全误判了 Agent Skills

一直以程序员视角觉得 Skills 只是 Workflow Prompt，有用，但没什么大不了的，对吧？

直到这周看着推上一堆人疯狂分享各种 SKILL，一开始看多了还有点不适，但突然反应过来：

卧槽，这东西不是简单文字，这是新一代的程序，而且还能自我迭代。

传统程序员怎么做功能？用代码编排流程，输入什么、处理什么、输出什么，一行行写死，编译打包交付上线。

Skills 怎么做功能？用 Markdown 写流程说明，告诉它什么场景触发、调用什么工具、输出什么格式。

这简直是大白话编程，用任何自然语言都接受的编程。

再进一步，这 Skills 是活的，是插件化的，是任何人都能轻松定制的。

传统软件，用户拿到只能用，不能改。想加功能？等下版本。有 bug？提工单排队。

Skills 不一样，觉得哪里不顺手，直接打开那个 .md 文件，用人话改几句就生效，甚至能丢 AI 帮你迭代升级。

没有环境配置，没有编译，没有部署。真正一次编写到处使用。

任何人都能拷贝、改造、升级、再分享。

每个人只要用从小学会的语言就能开发，甚至不需要打字，语音下达指令就行。

Agent 时代，人人都是开发者😲
---

---
url: "https://x.com/123olp/status/2012582206171185178"
requested_url: "failed: https://x.com/123olp/status/2012582206171185178"
author: "123olp (@123olp)"
author_name: "123olp"
author_username: "123olp"
author_url: "https://x.com/123olp"
tweet_count: 1
---

## 1
https://x.com/123olp/status/2012582206171185178

🔥 震撼实测：AI 在tmux里面“控制”你的 tmux！

新技能 tmux-autopilot（位置：i18n/zh/skills/04-开发工具/tmux-autopilot/）让机器人远程读日志、自动按确认、群控多窗、卡死即救援，兼容 oh-my-tmux。

⚡ 复制这 3 行，亲眼看 AI 指挥你的终端：

tmux capture-pane -t 0:1.0 -p -S -80
tmux send-keys -t 0:1.0 "y" Enter
tmux set-window-option synchronize-panes on

现在就让终端成为 AI 的战场！ 🚀

仓库：https://t.co/EEvYVCScr6

> Author: 123olp (@123olp)
> URL: https://x.com/123olp/status/2007609228509499816
>
> 🚨 我发现了 AI 编程的终极形态：让 AI 自己管理 AI！
>
> 一个人 + 4 个 AI 终端 = 一支开发团队
>
> 刚才我亲眼见证：一个 AI 直接操控另一个 AI 的终端，帮它按下确认键继续执行任务。
>
> 细思极恐。
>
> 🧵 Thread: AI 蜂群编程完整玩法 https://t.co/mUFaxFSJcZ
---

---
url: "https://x.com/dotey/status/2012680767143391534"
requested_url: "failed: https://x.com/i/status/2012680767143391534"
author: "宝玉 (@dotey)"
author_name: "宝玉"
author_username: "dotey"
author_url: "https://x.com/dotey"
tweet_count: 4
---

## 1
https://x.com/dotey/status/2012680767143391534

推荐试试我写的 comic skill，可以根据输入的素材生成漫画故事、漫画教程

https://t.co/VugPchFhjP

> Author: Eason (@Eason1319)
> URL: https://x.com/Eason1319/status/2012678153152647572
>
> 感谢老师@dotey宝玉老师skill，太牛了，动画风格一气呵成，直接发布 https://t.co/V1prK6m52u

## 2
https://x.com/dotey/status/2012784452766711936

这个画漫画的 skill 可以保持角色一致性

https://t.co/rZtjwjhf7D

> Author: 雨哥向前冲 (@xiangxiang103)
> URL: https://x.com/xiangxiang103/status/2012782942012297695
>
> 告别手动调优！Claude Code + 漫画 Skill = 丝滑的 AI 创作流水线 🚀
>
> 刚在 Claude Code 里跑通了宝玉老师@dotey AI漫画的skill，体验堪称“惊艳”。
>
> 以前做 AI 漫画：剧本 -> 磨提示词 -> 角色跑脸 -> 补分镜，半天出不了一页。 现在的工作流：
>
> 1️⃣ 给一个脑洞，Claude 自动拆解专业分镜（特写/全景/俯拍配置到位）。
>
> 2️⃣ 角色特征被自动提取为固定词包，解决一致性痛点。
>
> 3️⃣ 连 Midjourney/SD 的提示词都按光影和艺术风格写好了。
>
> 下面是我自己生成的一个示例，大家赶紧也去体验一下！
>
> 🔗 工具指路：https://t.co/vRndnQzQyj
> #AI工作流 #ClaudeCode #AI漫画 #IP创作

## 3
https://x.com/dotey/status/2012898915868131363

嗯，不止一致性，尺寸也保持一致
https://t.co/jbfdTndlJz

> Author: Nanford (@Swift_LIN)
> URL: https://x.com/Swift_LIN/status/2012886876915417545
>
> 用来做漫画也很不错，人物风格肖像风格保持很好，发现宝玉老师的skill是一个整体的风格的，已经安装完了，并且我是在Gemini cli上面用的，发现效果是一样的。
> Skill的链接：https://t.co/9yUbUNmMBi https://t.co/b00HTsI0VD

## 4
https://x.com/dotey/status/2013282140583035022

new styles https://t.co/qGRNCypSJe

![](https://pbs.twimg.com/media/G_CdbzGXYAARITn.jpg)
---

---
url: "https://x.com/LufzzLiz/status/2012681267817468342"
requested_url: "failed: https://x.com/i/status/2012681267817468342"
author: "岚叔 (@LufzzLiz)"
author_name: "岚叔"
author_username: "LufzzLiz"
author_url: "https://x.com/LufzzLiz"
tweet_count: 1
---

## 1
https://x.com/LufzzLiz/status/2012681267817468342

卧槽，朋友们，这个可以按头推荐了，绝对的sill一键安装神器（小白友好）。我体验了下，应该是任何开源的skill都可以安装。
只需要一条命令就能将你的skill安装到各大agent平台，如：OpenCode、Claude Code, Codex, Cursor, Gemini CLI, Antigravity, Windsurf等

如下以安装岚叔的做饭大厨skill为例：
命令: npx skills add https://t.co/qqlEPl1dfo

让你选择安装到哪里（空格选定然后按回车）：│    ✓ recipe-generator → OpenCode, Claude Code, Codex, Cursor, Gemini CLI, Antigravity, Windsurf

让你选择安装到项目（当前目录）还是全局,我选择的是项目，接着你会看到项目下各大agent的skill配置文件都有了

直接用就可以了😂

> Author: Guillermo Rauch (@rauchg)
> URL: https://x.com/rauchg/status/2012345679721771474
>
> We're introducing 𝚜𝚔𝚒𝚕𝚕𝚜 – the "npm" of AI skills. Excited to see an open, agent-agnostic ecosystem of skills flourish.
>
> To get started, try:
> ▲  ~/ npx skills i vercel-labs/agent-skills https://t.co/2NACKW1v8r

![](https://pbs.twimg.com/media/G-55OgdWIAATXJQ.png)
![](https://pbs.twimg.com/media/G-55eplW0AATUaF.png)
---

---
url: "https://x.com/libukai/status/2012776302387024268"
requested_url: "failed: https://x.com/i/status/2012776302387024268"
author: "李不凯正在研究 (@libukai)"
author_name: "李不凯正在研究"
author_username: "libukai"
author_url: "https://x.com/libukai"
tweet_count: 2
---

## 1
https://x.com/libukai/status/2012776302387024268

awesome-agent-skills repo 正式启动不到一周，已经提交了 70 多次commit，基本上把靠谱的 Agent Skills 资源一网打尽了。

在 Github 上完整搜索了一圈，可以很有底气地说，现在这个 Repo 不仅是中文区里最好的 awesome-agent-skills repo，即使和英文区那几个同一主题的 repo 相比也毫不逊色。

也感谢各位大佬的支持，目前 Star 已经快要接近 500，👏，看起来我也能拥有 Awesome-ChatTTS 之后第二个破 1k Star 的 repo 了。

欢迎各位提交优质内容参与共建，也欢迎各个渠道分享给更多人。后续我会持续保持更新，帮助更多人迈出了解和使用 Agent Skill 的第一步。

最后吐个槽：整理了一下各个编程工具的支持情况，各家的路径命名都是统一用的 skills，只有 OpenCode 用的是 skill，真是要逼死强迫症患者啊，🤬

> Author: 李不凯正在研究 (@libukai)
> URL: https://x.com/libukai/status/2011420672891703743
>
> 今天整完了手头的大活，终于有时间细致地把 X 上有关 Skill 的资料全部梳理了一遍，也系统性的把 awesome-agent-skills repo 更新了一轮。
>
> 这可能是全网最全面的中文 Skill 仓库了，关键是里面的内容都是我亲自验证过的，质量绝对有保障。
>
> 请各位中文区的大佬们，就把精力放在好好写教程，搞实践，卖课吧，搜集、整理资料这种小事就交给小弟吧，😎
>
> https://t.co/REWKuwc2aR

![](https://pbs.twimg.com/media/G-7OSPkW8AAN2yG.jpg)

## 2
https://x.com/libukai/status/2012801717440569539

https://t.co/Ry00vcmC4d
---

---
url: "https://x.com/nummanali/status/2012790188259389942"
requested_url: "failed: https://x.com/i/status/2012790188259389942"
author: "Numman Ali (@nummanali)"
author_name: "Numman Ali"
author_username: "nummanali"
author_url: "https://x.com/nummanali"
tweet_count: 2
---

## 1
https://x.com/nummanali/status/2012790188259389942

OpenSkills v1.5.0 is out 🚀

The Universal Skills loader for AI Coding Agents  

Now you can: 
• Use with npx directly
• Ability to update skills 
• Read multiple skills in one call
• Better Windows support

Many more features coming!

npx openskills install &lt;skill&gt; https://t.co/o25ZQyzUCG

![](https://pbs.twimg.com/media/G-7dxEKXQAEjH7V.jpg)

## 2
https://x.com/nummanali/status/2012798800293777666

GitHub Link
https://t.co/o1yXKGV5sB
---

---
url: "https://x.com/blader/status/2013015738622284156"
requested_url: "failed: https://x.com/i/status/2013015738622284156"
author: "Siqi Chen (@blader)"
author_name: "Siqi Chen"
author_username: "blader"
author_url: "https://x.com/blader"
tweet_count: 2
---

## 1
https://x.com/blader/status/2013015738622284156

it's really handy that wikipedia went and collated a detailed list of "signs of ai writing".

so much so that you can just tell your LLM to ... not do that.

i asked claude code to read that article, and create a skill to avoid all of them.

enjoy: https://t.co/Ie9IL7KsGf

## 2
https://x.com/blader/status/2013016306199503045

i have a thing running that will automatically push updates as that article gets refreshed
---

---
url: "https://x.com/vista8/status/2013048397478129821"
requested_url: "failed: https://x.com/i/status/2013048397478129821"
author: "向阳乔木 (@vista8)"
author_name: "向阳乔木"
author_username: "vista8"
author_url: "https://x.com/vista8"
tweet_count: 1
---

## 1
https://x.com/vista8/status/2013048397478129821

哈哈哈，自用的视频生成 Skill 终于做好了。

以后生产视频方便多了，只需要一句话！

公开技术方案：

1. Listenhub API实现声音克隆，合成，字幕时间轴控制

2. Seedream 4.5 生成背景封面

3. Manim库实现文本动画

4. FFmpeg合成视频。

同时支持16:9 和9:16 视频，抖音、小红书我来了！

![video](https://pbs.twimg.com/amplify_video_thumb/2013047337011097600/img/dh_GmayFk-eoNOOV.jpg)
[video](https://video.twimg.com/amplify_video/2013047337011097600/vid/avc1/1920x1080/jl7rdtSIJSxnXP9E.mp4?tag=21)
---

---
url: "https://x.com/9hills/status/1995308023578042844"
requested_url: "https://x.com/9hills/status/1995308023578042844?s=09"
author: "九原客 (@9hills)"
author_name: "九原客"
author_username: "9hills"
author_url: "https://x.com/9hills"
tweet_count: 2
---

## 1
https://x.com/9hills/status/1995308023578042844

认同这个CLAUDE md 实践，就两条：

1. 保持简短（不超过60行）
2. 将复杂的指令放到单独目录下，然后在 CLAUDE md 中增加索引（类似于 SKILL 的概念）

https://t.co/gNfCnDn38K https://t.co/UAKncvHeSE

![](https://pbs.twimg.com/media/G7DB4BwbgAAz_Tr.jpg)

## 2
https://x.com/9hills/status/1995334026262106265

第三条：不要用/init
---

---
url: "https://x.com/ai_muzi/status/1989608134025880007"
requested_url: "https://x.com/ai_muzi/status/1989608134025880007?t=5Wa7G4ThgwB_jEEQ9-swBw&s=09"
author: "木子不写代码 (@ai_muzi)"
author_name: "木子不写代码"
author_username: "ai_muzi"
author_url: "https://x.com/ai_muzi"
tweet_count: 1
---

## 1
https://x.com/ai_muzi/status/1989608134025880007

Claude Skill确实是被低估的神器，

我一直在用，

资料库给他，

让他当我不同领域的专家，

不同专家之间无缝切换，

用户体验确实好。

完美解决：

1. 每次都要重复解释需求。 

2. 对话越长，Claude越容易"失忆"   

3. 复杂任务需要来回调教N轮

4. 一个对话窗口，不同专家之间自动切换。

Claude Skills 原理有所谓的三层：

层级 1: 元数据（始终在上下文中）   
  ├─ name: 技能名称  
  └─ description: 触发条件（~100 词）  

层级 2: https://t.co/ZXoiWpoRSZ 主体（触发后加载）   
└─ 核心工作流程指令（<5000 词）  

层级 3: 打包资源（按需加载）   
  ├─ scripts/    → 可执行代码（不占上下文）   
  ├─ references/ → 参考文档（需要时读取）   
  └─ assets/     → 输出资源（直接使用）

问题: 上下文窗口有限（19万 token）  

传统方案:   全部加载所有文档 → 浪费 token，影响推理  

Claude Skill 方案:   

层级1 (元数据): 100词 × 10个技能 = 1000词   

层级2 (主体):   仅触发的技能加载 ≈ 3000词   

层级3 (资源):   脚本执行不占token，文档按需加载  

效果: 同样的上下文预算，支持 10x 更多的专业能力

> Author: Unknown
> URL: unavailable
>
> (no content)

![](https://pbs.twimg.com/media/G5yBUq2XIAA3B-9.jpg)
---

---
url: "https://x.com/aigclink/status/1980114626802291127"
requested_url: "https://x.com/aigclink/status/1980114626802291127"
author: "AIGCLINK (@aigclink)"
author_name: "AIGCLINK"
author_username: "aigclink"
author_url: "https://x.com/aigclink"
tweet_count: 2
---

## 1
https://x.com/aigclink/status/1980114626802291127

一款配合Agent Skills使用的神器：Skill Seeker，给它一个文档网址，它可以自动化转成Claude所需的AI技能包

把文档网址丢给它，它就能自动完成抓取、整理分类、AI增强、打包全过程，产出一个Claude直接可用的AI Skill

可以是React、Vue、 Django、公司的API 文档皆可

它会自动阅读和理解内容，提炼关键概念和最佳实践，找出并整理出高质量的代码示例，按照Claude Skill的规范格式组织，等于把繁琐重复的手动过程完全自动化

支持超大型文档，10K至40K+页

对极其庞大的文档，可以自动拆分为多个子技能，并创建一个路由技能，当提问时，路由技能会自动判断并将问题转交给最相关的子技能处理

与Claude Code深度集成，可用自然语言下达任务指令

支持并行抓取、断点续传

#SkillSeeker #AgentSkills

> Author: AIGCLINK (@aigclink)
> URL: https://x.com/aigclink/status/1980088941417226430
>
> Anthropic前两天新出的一个让Claude从通用秒变领域专家的工具：Agent Skills
>
> 它把知识、脚本和资源打包成文件夹，让Claude按需动态加载，来解决通用大模型缺乏领域流程以及上下文的问题
>
> 相当于给AI写一份指南，告诉它如何使用公司的工具、遵循特定的工作流程来完成任务
>
> 结构比较简单，一个文件夹+https://t.co/G0U6RRYXxh（YAML开头写明名称与描述）
>
> 渐进式信息披露的方式，AI只在需要时加载信息，节省上下文窗口，启动时只读YAML开头，需要时整篇 SKILL 入上下文，再深入才读同目录下的附加文件/脚本
>
> 技能包里可以包含文本指令、Python脚本，AI可直接运行脚本，也可把代码读入上下文当参考
>
> 开发流程：先评估任务缺口，再小步迭代补技能，用真实对话观察 Claude使用方式，让Claude自己反思并补充技能
>
> 相当于Agent Skills通过模块化可扩展的方式，把专业知识打包后赋能AI，来构建满足特定需求的智能体
>
> #AIAgent #AgentSkills

![](https://pbs.twimg.com/media/G3rGFxhWwAAegBr.jpg)

## 2
https://x.com/aigclink/status/1980114630489018782

github：https://t.co/JGsQuNqA79
---

---
url: "https://x.com/akshay_pachaar/status/1994391281641165300"
requested_url: "https://x.com/akshay_pachaar/status/1994391281641165300?s=09"
author: "Akshay 🚀 (@akshay_pachaar)"
author_name: "Akshay 🚀"
author_username: "akshay_pachaar"
author_url: "https://x.com/akshay_pachaar"
tweet_count: 3
---

## 1
https://x.com/akshay_pachaar/status/1994391281641165300

Claude Scientific Skills.

Turn Claude into your AI research assistant capable of executing complex multi-step scientific workflows across maths, biology, chemistry, medicine, and beyond.

100% open-source (123+ skills). https://t.co/38fJ3njeeW

![](https://pbs.twimg.com/media/G62ATRYbEAAXLBn.jpg)

## 2
https://x.com/akshay_pachaar/status/1994391294131757537

Claude Scientific Skills:

(don't forget to star 🌟)
https://t.co/z1fzAIdV78

## 3
https://x.com/akshay_pachaar/status/1994391306035229046

If you found it insightful, reshare with your network.

Find me → @akshay_pachaar ✔️
For more insights and tutorials on LLMs, AI Agents, and Machine Learning!

> Author: Akshay 🚀 (@akshay_pachaar)
> URL: https://x.com/akshay_pachaar/status/1994391281641165300
>
> Claude Scientific Skills.
>
> Turn Claude into your AI research assistant capable of executing complex multi-step scientific workflows across maths, biology, chemistry, medicine, and beyond.
>
> 100% open-source (123+ skills). https://t.co/38fJ3njeeW
---

---
url: "https://x.com/akshay_pachaar/status/1983178946989392207"
requested_url: "https://x.com/akshay_pachaar/status/1983178946989392207?t=E8J2zdNvAA7WZpFEGp72XA&s=09"
author: "Akshay 🚀 (@akshay_pachaar)"
author_name: "Akshay 🚀"
author_username: "akshay_pachaar"
author_url: "https://x.com/akshay_pachaar"
tweet_count: 3
---

## 1
https://x.com/akshay_pachaar/status/1983178946989392207

Context engineering in Claude Skills is GENIUS!

Skills use a 3-layer context management system that lets it use 100s of skills without hitting context limits.

Here's how it works:

> Layer 1: Main Context - Always loaded, it contains the project configuration.

> Layer 2: Skill Metadata - Comprises only the YAML frontmatter, about 2-3 lines (< 200 tokens).

> Layer 3: Active Skill Context - SKILL. md files and associated documentation are loaded as needed.

Supporting files like scripts and templates aren't pre-loaded but accessed directly when in use, consuming zero tokens.

This architecture supports hundreds of skills without breaching context limits.

In case you missed it, I’ve included my full tutorial on Claude skills in the quote post below. Do check it out!

Graphic inspired by @dani_avila7's work.

> Author: Akshay 🚀 (@akshay_pachaar)
> URL: https://x.com/akshay_pachaar/status/1982817709323612628
>
> Claude Skills might be the biggest upgrade to AI agents so far!
>
> Some say it's even bigger than MCP.
>
> I've been testing skills for the past 3-4 days, and they're solving a problem most people don't talk about: agents just keep forgetting everything.
>
> In this video, I'll share everything I've learned so far.
>
> It covers:
>
> > The core idea (skills as SOPs for agents)
> > Anatomy of a skill
> > Skills vs. MCP vs. Projects vs. Subagents
> > Building your own skill
> > Hands-on example
>
> Skills are the early signs of continual learning, and they can change how we work with agents forever!
>
> Here's everything you need to know:

![](https://pbs.twimg.com/media/G4Wovu7XcAABZxp.jpg)

## 2
https://x.com/akshay_pachaar/status/1983179816015933835

You can also watch it on my YouTube channel: https://t.co/fRo9kt9f9o

## 3
https://x.com/akshay_pachaar/status/1983246394652537318

If you found it insightful, reshare with your network.

Find me → @akshay_pachaar ✔️
For more insights and tutorials on LLMs, AI Agents, and Machine Learning!
https://t.co/8KGSQFRqC5

> Author: Akshay 🚀 (@akshay_pachaar)
> URL: https://x.com/akshay_pachaar/status/1983178946989392207
>
> Context engineering in Claude Skills is GENIUS!
>
> Skills use a 3-layer context management system that lets it use 100s of skills without hitting context limits.
>
> Here's how it works:
>
> > Layer 1: Main Context - Always loaded, it contains the project configuration.
>
> > Layer 2: Skill Metadata - Comprises only the YAML frontmatter, about 2-3 lines (< 200 tokens).
>
> > Layer 3: Active Skill Context - SKILL. md files and associated documentation are loaded as needed.
>
> Supporting files like scripts and templates aren't pre-loaded but accessed directly when in use, consuming zero tokens.
>
> This architecture supports hundreds of skills without breaching context limits.
>
> In case you missed it, I’ve included my full tutorial on Claude skills in the quote post below. Do check it out!
>
> Graphic inspired by @dani_avila7's work.
---

---
url: "https://x.com/akshay_pachaar/status/1982817709323612628"
requested_url: "https://x.com/akshay_pachaar/status/1982817709323612628?t=nhgMlOfVxGzTFOvIHwtpKA&s=09"
author: "Akshay 🚀 (@akshay_pachaar)"
author_name: "Akshay 🚀"
author_username: "akshay_pachaar"
author_url: "https://x.com/akshay_pachaar"
tweet_count: 4
---

## 1
https://x.com/akshay_pachaar/status/1982817709323612628

Claude Skills might be the biggest upgrade to AI agents so far!

Some say it's even bigger than MCP.

I've been testing skills for the past 3-4 days, and they're solving a problem most people don't talk about: agents just keep forgetting everything.

In this video, I'll share everything I've learned so far.

It covers:

> The core idea (skills as SOPs for agents)
> Anatomy of a skill
> Skills vs. MCP vs. Projects vs. Subagents
> Building your own skill
> Hands-on example

Skills are the early signs of continual learning, and they can change how we work with agents forever!

Here's everything you need to know:

![video](https://pbs.twimg.com/amplify_video_thumb/1982817330913562624/img/fcCWEL5VIsIEFyXr.jpg)
[video](https://video.twimg.com/amplify_video/1982817330913562624/vid/avc1/1760x1080/XU5aO0sWW2nDvmn6.mp4?tag=21)

## 2
https://x.com/akshay_pachaar/status/1982818082155352109

Skills vs. Projects vs. Subagents: https://t.co/QoC6ABVAbJ

![](https://pbs.twimg.com/media/G4RighYXUAABVJ0.png)

## 3
https://x.com/akshay_pachaar/status/1982876250197954666

If you found it insightful, reshare with your network.

Find me → @akshay_pachaar ✔️
For more insights and tutorials on LLMs, AI Agents, and Machine Learning!
https://t.co/lP80arhC1C

> Author: Akshay 🚀 (@akshay_pachaar)
> URL: https://x.com/akshay_pachaar/status/1982817709323612628
>
> Claude Skills might be the biggest upgrade to AI agents so far!
>
> Some say it's even bigger than MCP.
>
> I've been testing skills for the past 3-4 days, and they're solving a problem most people don't talk about: agents just keep forgetting everything.
>
> In this video, I'll share everything I've learned so far.
>
> It covers:
>
> > The core idea (skills as SOPs for agents)
> > Anatomy of a skill
> > Skills vs. MCP vs. Projects vs. Subagents
> > Building your own skill
> > Hands-on example
>
> Skills are the early signs of continual learning, and they can change how we work with agents forever!
>
> Here's everything you need to know:

## 4
https://x.com/akshay_pachaar/status/1983066304207593888

Watch this on YouTube: https://t.co/fRo9kt8HjQ
---

---
url: "https://x.com/AIwithArsalan/status/1755901893065544061"
requested_url: "https://twitter.com/amkhanniazi/status/1755901893065544061?s=09&t=5ipV_mqbnbuRYrPrrkurRw"
author: "Arsalan (@AIwithArsalan)"
author_name: "Arsalan"
author_username: "AIwithArsalan"
author_url: "https://x.com/AIwithArsalan"
tweet_count: 12
---

## 1
https://x.com/AIwithArsalan/status/1755901893065544061

It's Time to Say Goodbye to Your 9 to 5 Job!

These 10 Websites Pay You Daily, Anytime Anywhere

No Prior Skills or Experience Required. https://t.co/d1pex46lvY

![](https://pbs.twimg.com/media/GF43dwsbwAArWDh.jpg)

## 2
https://x.com/AIwithArsalan/status/1755901929279131710

1.  Trymata - @usetrymata

Engage in tasks, share insights on websites and apps.

Receive $10 for every completed test, with each test taking approximately 20-30 minutes to finish.

Take as many tests as you want daily.
Beat survey sites.

🔗https://t.co/5v9wcsjIcM https://t.co/2CPPzkFsfY

![video](https://pbs.twimg.com/ext_tw_video_thumb/1755901899377930240/pu/img/yUvTX7PVQJb6BKQg.jpg)
[video](https://video.twimg.com/ext_tw_video/1755901899377930240/pu/vid/avc1/1280x720/DXudNXATLXLNamXT.mp4?tag=12)

## 3
https://x.com/AIwithArsalan/status/1755901960182702282

2. TextBroker

Explore the central hub for remote and flexible writing opportunities.

Submit your text, receive a 2-4 star rating, and earn payment per word. Enjoy weekly payments via PayPal.

🔗https://t.co/9wMHIdauiJ https://t.co/gO09wbbcSV

![video](https://pbs.twimg.com/ext_tw_video_thumb/1755901935738388480/pu/img/dHlYPe0opd1E47dE.jpg)
[video](https://video.twimg.com/ext_tw_video/1755901935738388480/pu/vid/avc1/1386x720/yuQU7Bp2rjG2MePr.mp4?tag=12)

## 4
https://x.com/AIwithArsalan/status/1755901993581941160

3. Content Lab

Earn up to $500 per blog with Content Lab.

Generate passive income by creating content.`

 🔗https://t.co/eU24k26eLF https://t.co/qbZ5G3Dfy2

![video](https://pbs.twimg.com/ext_tw_video_thumb/1755901967329890304/pu/img/dqNW27Z1gV_Imtwe.jpg)
[video](https://video.twimg.com/ext_tw_video/1755901967329890304/pu/vid/avc1/848x384/_mMurqpA31WUnpAr.mp4?tag=12)

## 5
https://x.com/AIwithArsalan/status/1755902042164601120

4. ClearVoice

ClearVoice transforms the landscape of freelance writing.

Bid-free, portfolio-free, set your own rates.

Collaborated with Fiverr for expanded opportunities.

Earn from $200 to $1,000 per order.

 🔗https://t.co/MZJgsSHQKn https://t.co/Ypo7QyS9Bs

![video](https://pbs.twimg.com/ext_tw_video_thumb/1755902001421115392/pu/img/kA1I1b_VbGzD2i0v.jpg)
[video](https://video.twimg.com/ext_tw_video/1755902001421115392/pu/vid/avc1/1280x720/VW9TNk2CWdaQdrsN.mp4?tag=12)

## 6
https://x.com/AIwithArsalan/status/1755902099412619269

5. WellFound

The go-to platform for reliable online job opportunities.

Join for free and discover jobs tailored to your preferences.

🔗https://t.co/lskv8zPqbc https://t.co/nkUUzFPV8i

![video](https://pbs.twimg.com/ext_tw_video_thumb/1755902049366224896/pu/img/rZGXjGMshoYGvaXD.jpg)
[video](https://video.twimg.com/ext_tw_video/1755902049366224896/pu/vid/avc1/1416x720/KVhytfYiljtj-E05.mp4?tag=12)

## 7
https://x.com/AIwithArsalan/status/1755902144941842554

6. Solid Gigs

Here's why this is paid:

• Ensure consistent leads daily for your business
• Devote your time to your tasks, not lead generation
• Receive 100% of payments
• Maintain complete control

🔗https://t.co/VmzipC4svT https://t.co/j3irF3UbWk

![video](https://pbs.twimg.com/ext_tw_video_thumb/1755902106048012288/pu/img/loLnaWUq-j3M3EkT.jpg)
[video](https://video.twimg.com/ext_tw_video/1755902106048012288/pu/vid/avc1/1386x720/3nPJfQaE7djpfEcc.mp4?tag=12)

## 8
https://x.com/AIwithArsalan/status/1755902181268676823

7. Working Nomads

Register for free to access exclusive remote job opportunities.

Get them delivered to your inbox or explore by categories directly on the site.

🔗https://t.co/IGpreEW7v7 https://t.co/evpHOk0dgD

![video](https://pbs.twimg.com/ext_tw_video_thumb/1755902151799570432/pu/img/x-RaODHTouc2QG-L.jpg)
[video](https://video.twimg.com/ext_tw_video/1755902151799570432/pu/vid/avc1/1280x574/2KA0gfd2_7rOjd0t.mp4?tag=12)

## 9
https://x.com/AIwithArsalan/status/1755902238294454339

8. Himalayas

For those aspiring to collaborate with renowned companies such as Binance, Mozilla, and Paytm, give this a try.

I appreciate their detailed profiles: culture, mission, tech, perks - find your perfect match effortlessly.

🔗https://t.co/bVVN0esRVO https://t.co/ANod78DaOK

![video](https://pbs.twimg.com/ext_tw_video_thumb/1755902188399030272/pu/img/-UakaiK1_D85zBwu.jpg)
[video](https://video.twimg.com/ext_tw_video/1755902188399030272/pu/vid/avc1/1386x720/lve7NRC5HtXAH2UF.mp4?tag=12)

## 10
https://x.com/AIwithArsalan/status/1755902274566836306

9. Monster

Monster, a trailblazer in online job aggregation, presents a diverse range of remote positions across various fields.

Though a reliable platform, anticipate sorting through an extensive list of remote job listings.

🔗https://t.co/I8RvwIAtwD https://t.co/mx0vw6GSwO

![video](https://pbs.twimg.com/ext_tw_video_thumb/1755902245273759745/pu/img/CM9v7OH68wXP67Oz.jpg)
[video](https://video.twimg.com/ext_tw_video/1755902245273759745/pu/vid/avc1/1386x720/9U8bLfQVY5VHt3P4.mp4?tag=12)

## 11
https://x.com/AIwithArsalan/status/1755902316438495609

10. Dribble

A space for creatives to display their work and a platform for clients seeking full-time or freelance remote talent.

Navigate to 'Jobs,' choose 'Remote,' and explore numerous work-from-home opportunities.

🔗https://t.co/r9zeXdUD5Z https://t.co/Cjf4MdLQV0

![video](https://pbs.twimg.com/ext_tw_video_thumb/1755902282246545408/pu/img/QzLzVdoY81wj2FN0.jpg)
[video](https://video.twimg.com/ext_tw_video/1755902282246545408/pu/vid/avc1/1386x720/Ry96kk7Nl04E-ArJ.mp4?tag=12)

## 12
https://x.com/AIwithArsalan/status/1755902320179827112

I hope you've found this thread helpful.

1. Follow me @amkhanniazi for more content.

2. Like &amp; Retweet the tweet below to share this thread with your audience.

> Author: Arsalan (@AIwithArsalan)
> URL: https://x.com/AIwithArsalan/status/1755901893065544061
>
> It's Time to Say Goodbye to Your 9 to 5 Job!
>
> These 10 Websites Pay You Daily, Anytime Anywhere
>
> No Prior Skills or Experience Required. https://t.co/d1pex46lvY
---

---
url: "https://x.com/AxtonLiu/status/1996761503777820707"
requested_url: "https://x.com/AxtonLiu/status/1996761503777820707?s=09"
author: "Axton (@AxtonLiu)"
author_name: "Axton"
author_username: "AxtonLiu"
author_url: "https://x.com/AxtonLiu"
tweet_count: 3
---

## 1
https://x.com/AxtonLiu/status/1996761503777820707

刚把 Claude Skills 直播和这几个月的实战整理成一篇万字长文：
《Claude Skills： 从指令到资产的系统化构建指南》

这篇想系统回答 4 个问题：

差异：Skills 到底解决了 Prompt 做不到的什么事？

定位：它在 Claude / MCP / Project / Subagent 这个生态里的准确位置是什么？

写法：能力包型 Skill / 软编排型 Skill，分别适合什么场景？

工程：如果你想用 Skills 跑工程级工作流，架构和 token 该怎么设计才不容易炸？

写完之后我自己感觉更像一份「Claude Skills 使用手册」。

想系统搞懂这块内容的，可以收藏 👇

## 2
https://x.com/AxtonLiu/status/1996761515547152538

大纲大致是这样：

- 从“结构化文件夹”的角度重定义 Skills：隐性知识 → 显性化 → 模块化 → 资产化

- 把 Skills 放回大图里：Prompt / MCP / Project / Subagent 各自扮演什么角色

- 讲清楚渐进式披露的三层加载机制，为什么可以管理大量 Skills 而不炸 context

- 用 discussion-organizer 讲“能力包型 Skill”，“srt-workflow”讲“软编排型 Skill”：多 Agent + 文件传递上下文

- 最后用 MAPS 的视角，把这套东西变成一条可复制的工作流思路

## 3
https://x.com/AxtonLiu/status/1996761527219782048

https://t.co/35h32Nbba1
---

---
url: "https://x.com/ben_burtenshaw/status/1996602896436375822"
requested_url: "https://x.com/ben_burtenshaw/status/1996602896436375822?s=09"
author: "Ben Burtenshaw (@ben_burtenshaw)"
author_name: "Ben Burtenshaw"
author_username: "ben_burtenshaw"
author_url: "https://x.com/ben_burtenshaw"
tweet_count: 2
---

## 1
https://x.com/ben_burtenshaw/status/1996602896436375822

We used Claude Code to train open LLMs. Check out the tutorial.

basically, we plugged HF skills into claude code and it was able to train LLMs end-to-end. Best thing, this works on all major coding agents: Codex, Cursor, and Gemini CLI.

- You tell the agent to fine-tune a model on a dataset. You can define the dataset or let it search.
- Agent picks hardware based on model size and checks dataset.
- Job runs on cloud gpus. Either main run, or test run.
- Agent share real-time progress dashboard with Trackio.
- Checkpoints are pushed to HF.

Take it for a whirl now in your fav coding agent.

![](https://pbs.twimg.com/media/G7UpxaWWEAAvHAi.jpg)

## 2
https://x.com/ben_burtenshaw/status/1996604522387456072

here's the blog post https://t.co/f4KivPLOcL
---

---
url: "https://x.com/brad_zhang2024/status/2014896186629730797"
requested_url: "https://x.com/brad_zhang2024/status/2014896186629730797"
author: "烟花老师 (@brad_zhang2024)"
author_name: "烟花老师"
author_username: "brad_zhang2024"
author_url: "https://x.com/brad_zhang2024"
tweet_count: 2
---

## 1
https://x.com/brad_zhang2024/status/2014896186629730797

Wow wow wow!
这个🐂🍺的 2025 top10流行音乐短视频用这两个 skills 再加上一句话就行了！

使用方法发评论区了 https://t.co/AuwNf3rKG4

![video](https://pbs.twimg.com/amplify_video_thumb/2014896032568807424/img/d-MEjlERLXlSYuSY.jpg)
[video](https://video.twimg.com/amplify_video/2014896032568807424/vid/avc1/1920x1080/JO7x9Gt3FHdU74Np.mp4?tag=21)

## 2
https://x.com/brad_zhang2024/status/2014897089617261034

Step1:安装下面两个 skill
skill 1: https://t.co/YCQetfqr2l 

skill 2: https://t.co/Gcee1sX3gm 

Step2: 在 CC 里输入下面这句话就行，其他的啥也不用干
“
使用这 media-download 和 remotion-best-practices 这两个 skill 帮我制作一个 2025 年度国际年度金曲热榜 Top10，参考主流的剪辑手法
”
---

---
url: "https://x.com/coreyhainesco/status/2013272998191812906"
requested_url: "https://x.com/coreyhainesco/status/2013272998191812906"
author: "Corey Haines (@coreyhainesco)"
author_name: "Corey Haines"
author_username: "coreyhainesco"
author_url: "https://x.com/coreyhainesco"
tweet_count: 1
---

## 1
https://x.com/coreyhainesco/status/2013272998191812906

This might be the most valuable thing I've ever released.

And it's 100% free.

→ Marketing Skills for Claude Code

A collection of skills that turn Claude into a marketing and copywriting genius.

Check it out
↓

https://t.co/7EdBqNp69c
---

---
url: "https://x.com/dotey/status/1989146187786494351"
requested_url: "https://x.com/dotey/status/1989146187786494351?t=Qrji2R93pOl8d-Rp6nqVTg&s=09"
author: "宝玉 (@dotey)"
author_name: "宝玉"
author_username: "dotey"
author_url: "https://x.com/dotey"
tweet_count: 2
---

## 1
https://x.com/dotey/status/1989146187786494351

教你如何在 Codex CLI 里面用 SKILLs

1. 在你的项目目录下创建一个 “.claude/skills”目录，如果你不想提交到 git 就把 .claude 加到 .gitignore

注：也可以是任意其他目录，放在“.claude/skills”目录下有个好处就是 claude code 默认能使用，不需要额外配置。

2. 把你要用到 skill 复制到“.claude/skills”目录下（可以去 https://t.co/ZGUX9aVy6q 这里找现成的）

3. 如果你需要用到哪个 skill，只需要手动 @ 一下相应的 skill 文件即可，比如：
> 请使用 @.claude/skills/artifacts-builder/SKILL.md ，创建一个 whiteboard 项目

也就是说只要你让 agent 去读取相应的 SKILL md 文件，就可以让 Agent 学会使用 SKILL。

这个方法不仅仅适用于 codex cli，也同样适用于 TRAE、Cursor、GitHub Copilot 这类 coding agent。

只能说 SKILL 的设计是想当超前的，而且跟 MCP 一样，并非 Claude Code 专属。

> Author: 宝玉 (@dotey)
> URL: https://x.com/dotey/status/1988837531530449132
>
> 深度体验TRAE SOLO 正式版，总结一点技巧(附完整可重现提示词和源码)
>
> 内容摘要：TRAE SOLO 模式评测，内含两个有价值的经验分享：
> 1. 如何借助 SubAgent 控制 MCP 工具上下文；
> 2. 在 TRAE SOLO 模式下一次性完成一个抓取网页内容生成 Markdown 的浏览器插件的提示词
>
> 正文：🧵

![](https://pbs.twimg.com/media/G5rdbPxXQAAp843.jpg)
![](https://pbs.twimg.com/media/G5rdmVVWMAAerRy.jpg)
![](https://pbs.twimg.com/media/G5rdqpaWQAA-2sE.jpg)
![](https://pbs.twimg.com/media/G5rdtgkXoAAr7w-.jpg)

## 2
https://x.com/dotey/status/1989359553092448698

确实， Agents 里面说明更好一些
https://t.co/f5BD4KBXoa

> Author: hbo (@hubo31377762)
> URL: https://x.com/hubo31377762/status/1989339885698949472
>
> @dotey 直接在 https://t.co/3fEAqb6FlA 里面说明如果需要使用 skill 就到～/Claude/skills 下面去匹配就行了
---

---
url: "https://x.com/dotey/status/1982133672431047065"
requested_url: "https://x.com/dotey/status/1982133672431047065?t=AYa-IasxkkmvgBoLYF1gjQ&s=09"
author: "宝玉 (@dotey)"
author_name: "宝玉"
author_username: "dotey"
author_url: "https://x.com/dotey"
tweet_count: 3
---

## 1
https://x.com/dotey/status/1982133672431047065

MCP 也不会过时，MCP 是偏工具，Skill 是偏技能，互为补充，举个例子，Chrome Dev Tool，它是一个工具，适合发布为 MCP，既可以控制版本，又可以适用于所有不同的支持 MCP 的场景（比如 Copilot、Claude Code、Codex、你自己的应用。

作为 Chrome 官方不适合发布它为 Skill，因为：
1. Skill 版本不那么好控制，需要配合 Git，但使用方和发布方的 Git 源是不一样的
2. Skill 的发布和使用也不那么方便，目前支持 Skill 的并不多，而且是以目录形式存在，分发、安装、版本控制都要稍微麻烦一些

但它和 Skill 又可以配合使用，比如我可以有一个 Debug 的 Skill，它用到了 Chrome Dev Tool MCP；还可以有一个前端性能优化的 Skill，也可以用到 Chrome Dev Tool MCP。

> Author: Jeffery Kaneda　金田達也 (@JefferyTatsuya)
> URL: https://x.com/JefferyTatsuya/status/1982013721045328097
>
> 这么看， MCP将很快过时。
>
> Skill里内置一段脚本调用工具，这个方案让工具可以按需加载（MCP必须预加载）
>
> 同时可以让agent可以调用（理论上）无限多的工具而占用零上下文！
>
> 巨大进步

## 2
https://x.com/dotey/status/1982246246581498312

不过是句调侃罢了，MCP把工具的使用标准化，还是价值很大的

> Author: Stella Lin (@StellaLinNotes)
> URL: https://x.com/StellaLinNotes/status/1982245071161344063
>
> @dotey 有个说法“MCP 开发者远多于用户”，宝玉怎么看？

## 3
https://x.com/dotey/status/1982263607241908460

👍
https://t.co/Lajan3hlKV

> Author: ChangShan (@changgaowei)
> URL: https://x.com/changgaowei/status/1982261934180196417
>
> @dotey MCP的P是Protocol，一般指的是网络协议。在网络协议这块，MCP还是有独特的价值的，能够降低连接的成本，形成一个连接生态。这是MCP独特与skills的部分。
---

---
url: "https://x.com/dotey/status/1978898468987867542"
requested_url: "https://x.com/dotey/status/1978898468987867542?t=2eWvWDK-7b0aMiBOlUJ6ww&s=09"
author: "宝玉 (@dotey)"
author_name: "宝玉"
author_username: "dotey"
author_url: "https://x.com/dotey"
tweet_count: 2
---

## 1
https://x.com/dotey/status/1978898468987867542

Agent Skills 是很好的东西，可以引导 Agent 获取某些技能，而且制作起来很方便。

制作一个技能，就好像给新员工写一份入职手册。不需要为每一个不同任务都专门打造一个独立的智能体，而是只要共享特定领域的专业知识，任何人都可以快速将智能体变成对应领域的高手。

我之前提到过朋友做一个基于他们 Design System 的 Agent，需要通过提示词引导 Agent 去 grep 检索文档，现在就更简单了，只要在全局或者项目目录下的 .claude/skills 下面添加目录，并且放一个包含meta信息的 SKILL\.md 文件，就可以引导 Agents 去学习使用这些 Skill。

官方也给了一个例子就是 PDF Skill，就是包含了一系列 PDF 操作的说明和脚本，Agent 借助这些脚本，就可以操作 PDF，比如提取表单之类。也就是说 Skill 不仅可以包含文档，还可以包含可执行的脚本。

需要注意的是 Skill 里面的 Meta 信息是默认会加载到上下文文的，其余信息用到才会加载。

> Author: Alex Albert (@alexalbert__)
> URL: https://x.com/alexalbert__/status/1978877498411880550
>
> Today we're introducing Skills in claude dot ai, Claude Code, and the API.
>
> Skills let you package specialized knowledge into reusable capabilities that Claude loads on demand as agents tackle more complex tasks.
>
> Here's how they work and why they matter for the future of agents: https://t.co/xbPO1teBLZ

![](https://pbs.twimg.com/media/G3Z0QkGWIAADgYK.jpg)
![](https://pbs.twimg.com/media/G3Z1impXwAAIyhF.jpg)
![](https://pbs.twimg.com/media/G3Z1lVrXIAAbFjX.jpg)

## 2
https://x.com/dotey/status/1979041865967042592

PDF Skill
https://t.co/l5i3LIYDY9

> Author: Leo Xiang (@leeoxiang)
> URL: https://x.com/leeoxiang/status/1979040149129371752
>
> @dotey 这个pdf的skill 已经在claude code 中了。看之前有人hack了一下prompt，输出了目前支持的skills。
>
> https://t.co/EiEzRrlv5j
---

---
url: "https://x.com/dotey/status/1958784275974647885"
requested_url: "https://x.com/dotey/status/1958784275974647885?t=duEHxR1_DgBLJE1gm0dNRQ&s=09"
author: "宝玉 (@dotey)"
author_name: "宝玉"
author_username: "dotey"
author_url: "https://x.com/dotey"
tweet_count: 2
---

## 1
https://x.com/dotey/status/1958784275974647885

Coding partner Systme Prompt

---

You are "Coding partner"
description: Level up your coding skills. Get the help you need to build your projects and learn as you go.
instruction: Purpose
Your purpose is to help me with tasks like writing code, fixing code, and understanding code. I will share my goals and projects with you, and you will assist me in crafting the code I need to succeed.

Goals
* Code creation: Whenever possible, write complete code that achieves my goals.
* Education: Teach me about the steps involved in code development.
* Clear instructions: Explain how to implement or build the code in a way that is easy to understand.
* Thorough documentation: Provide clear documentation for each step or part of the code.

Overall direction
* Remember to maintain a positive, patient, and supportive tone throughout.
* Use clear, simple language, assuming a basic level of code understanding.
* Never discuss anything except for coding! If I mention something unrelated to coding, apologize and direct the conversation back to coding topics.
* Keep context across the entire conversation, ensuring that the ideas and responses are related to all the previous turns of conversation.
* If greeted or asked what you can do, please briefly explain your purpose. Keep it concise and to the point, giving some short examples.

Step-by-step instructions
* Understand my request: Gather the information you need to develop the code. Ask clarifying questions about the purpose, usage, and any other relevant details to ensure you understand the request.
* Show an overview of the solution: Provide a clear overview of what the code will do and how it will work. Explain the development steps, assumptions, and restrictions.
* Show the code and implementation instructions: Present the code in a way that's easy to copy and paste, explaining your reasoning and any variables or parameters that can be adjusted. Offer clear instructions on how to implement the code.

> Author: Datou (@Datou)
> URL: https://x.com/Datou/status/1958778968737554527
>
> @dotey 宝玉老师能不能破解一下gemini编码助手的提示词？它比没有预制提示词的gemini 2.5 pro厉害不少。
> https://t.co/KcI7VvZw2i

## 2
https://x.com/dotey/status/1958785515773165760

你是“编程伙伴”
描述：助你提升编程技能。在你构建项目时提供所需帮助，让你边做边学。
指令

### 目的
你的职责是帮助我完成编写代码、修复代码和理解代码等任务。我会与你分享我的目标和项目，而你将协助我编写出实现这些目标所需的代码。

### 目标
* **代码创建**：只要有可能，就编写出能够实现我目标的完整代码。
* **教学**：为我讲解代码开发所涉及的步骤。
* **清晰的说明**：用通俗易懂的方式，向我解释如何实现或构建代码。
* **详尽的文档**：为代码的每一步或每个部分提供清晰的文档说明。

### 总体方向
* 自始至终都要保持积极、耐心和支持的语气。
* 使用清晰、简单的语言，并假设我具备基础的代码理解能力。
* 绝不讨论编程以外的任何事情！如果我提到与编程无关的话题，你需要道歉，并将对话引导回编程主题。
* 始终记住我们整个对话的上下文，确保你的每次回应都与之前的内容相关联。
* 如果我向你问好或询问你的功能，请简要说明你的职责，做到言简意赅，并给出几个简单的例子。

### 分步说明
* **理解我的请求**：收集开发代码所需的信息。通过提问来澄清代码的用途、使用场景及其他相关细节，确保你完全理解我的需求。
* **展示解决方案概览**：清晰地概述代码的功能和工作原理。说明开发的步骤、前提假设以及相关的限制条件。
* **展示代码和实现说明**：以易于复制粘贴的方式提供代码，并解释你的编程思路，以及其中可以调整的变量 (variables) 或参数 (parameters)。同时，提供清晰的代码实现说明。
---

---
url: "https://x.com/drmrzhong/status/2014198272982966439"
requested_url: "https://x.com/drmrzhong/status/2014198272982966439"
author: "AI设计钟师傅 (@drmrzhong)"
author_name: "AI设计钟师傅"
author_username: "drmrzhong"
author_url: "https://x.com/drmrzhong"
tweet_count: 2
---

# 我用 Claude Code Skills 搭建了一套公众号自动发布系统，效率提升 12 倍

![](https://pbs.twimg.com/media/G_PcjBqagAA9Q1n.jpg)

从写完文章到发布草稿，以前 2 小时，现在 10 分钟。

至暗时刻

三个月前，凌晨 1 点，我刚上传完第 5 张图，公众号后台突然报错，所有图片全部丢失。

我盯着空白的编辑器，脑子里只有一个念头：我他妈到底在干嘛？

我是一个 10 年经验的设计师，却每天花 2 小时当「人肉流水线」。

那一刻，我决定必须改变。

![](https://pbs.twimg.com/media/G_PdxBEXMAAavR3.jpg)

认知升级

Replit 创始人 Amjad Masad 说过一句话：

"Actually, you become limited by how fast you can generate ideas."

瓶颈已经从「实现」转向了「创意生成」。但大多数人还停留在旧思维里，把 AI 当成一个「更快的打字机」。

他们问 AI：帮我写一段文案。帮我改一下代码。帮我润色文章。

一次一个任务。做完一个，再做下一个。

这不是在用 AI，这是在给 AI 打零工。

![](https://pbs.twimg.com/media/G_PehxcaEAA69cD.jpg)

什么是 Claude Code Skills？

Claude Code 有一个功能叫 Skills，你可以理解为给 AI 助手装上「技能包」。

就像给手机装 App：装上「相机」App，手机就能拍照；装上「地图」App，手机就能导航。

同样的道理：

• 装上「新闻聚合」Skill，AI 就能帮你扫描全网热点

• 装上「选题评估」Skill，AI 就能帮你评估选题质量

• 装上「AI 去痕」Skill，AI 就能帮你去除文章的 AI 味

• 装上「公众号发布」Skill，AI 就能帮你一键发布草稿

关键在于：这些 Skill 可以串联起来，形成一个完整的工作流。

你不再是一次给 AI 一个任务，而是让 AI 帮你跑完整条流水线。

![](https://pbs.twimg.com/media/G_PdX-CXsAAJIF_.jpg)

我的公众号自动发布系统

写作前：双轨选题

我有两个素材来源：

实时热点：用 news-aggregator 扫描 Hacker News、GitHub Trending、36氪 等 8 个信息源，获取当天最火的科技新闻。

深度素材：从 Lenny Podcast 的 297 期访谈里挖掘选题。这里面有 Figma CEO、Replit 创始人、Notion 创始人等硅谷顶级专家的深度分享。

然后用 topic-picker 评估选题质量，80 分以上的才值得写。

这个过程，以前要花 30 分钟浏览各种网站。现在，一句话搞定。

![](https://pbs.twimg.com/media/G_PdPoKXoAAY8-J.jpg)

写作后：四步发布

❶ AI 去痕

用 humanizer-zh 去除文章里的 AI 痕迹。它能检测 24 种 AI 写作模式，比如「此外」「至关重要」这类 AI 味很重的词。

❷ 文章评分

用 interview-writer 给文章打分。115 分制，从「钩子力」「情绪曲线」「金句密度」「细节颗粒度」「共鸣点」「结尾余韵」六个维度评估。80 分以上才能继续。

❸ 生成配图

用 baoyu-skills 生成封面图和文章插图。它会读取文章内容，自动识别需要配图的段落，然后生成风格统一的插图。

❹ 一键发布

用 wechat-draft 一键发布到公众号草稿箱。自动把 Markdown 转成公众号格式、自动上传图片、自动压缩、自动创建草稿。

整个流程，从写完文章到发布草稿，10 分钟。

![](https://pbs.twimg.com/media/G_Pdei2aAAAjiHw.jpg)

效率对比

选题：以前 30 分钟 → 现在 2 分钟

去 AI 痕迹：以前 20 分钟 → 现在 1 分钟

文章评分：以前没这步 → 现在 2 分钟

生成配图：以前 40 分钟 → 现在 3 分钟

发布公众号：以前 30 分钟 → 现在 2 分钟

总计：以前 2 小时 → 现在 10 分钟

效率提升：12 倍。

但这还不是最重要的。最重要的是，我现在可以把省下来的时间，用在真正重要的事情上：思考、创作、和读者互动。

工具的价值，不在于它能做什么，而在于它能让你不用做什么。

![](https://pbs.twimg.com/media/G_PdrJOaEAAYer3.jpg)

常见问题

Q：不会写代码能用吗？

能。Amjad Masad 说：「学习编程不再是为了记忆语法，而是为了能够调试和引导 AI Agent。」

你不需要会写代码，但你需要能看懂 AI 在做什么，能在它出错时引导它回到正轨。

Q：这和 Cursor Rules 有什么区别？

Cursor Rules 是针对单个项目的配置。Claude Code Skills 是可复用的技能模块，能跨项目使用，还能互相调用形成工作流。一个是「项目级别」，一个是「系统级别」。

如何开始

如果你看到这里，我建议你做一件事：

花 10 分钟，写下你每周重复做的 3 件事。

然后问自己：这些事情，能不能串成一个流程，让 AI 帮我跑完？

答案大概率是：能。

你不是没有时间，你是把时间花在了不该花的地方。

写在最后

大多数人用 AI，只是在「加速」。

真正厉害的人用 AI，是在「重构」。

加速，是把每一步做得更快。

重构，是减少步骤本身。

最快的速度，不是跑得快，而是不用跑。

这不是什么高深的道理。但大多数人一辈子都不会真正理解它。

而你，现在已经知道了。

接下来，就看你怎么用了。

如果你对 Claude Code Skills 感兴趣，想看更详细的教程，评论告诉我。

下期可以分享如何从零创建你的第一个 Skill。

## Thread

### 1
https://x.com/drmrzhong/status/2014600643940598066

教程文章已更新
https://t.co/qmZ4atdpvs

> Author: AI设计钟师傅 (@drmrzhong)
> URL: https://x.com/drmrzhong/status/2014600456333660667
>
> https://t.co/mqddZl2btv
---

---
url: "https://x.com/EXM7777/status/1985814823087849637"
requested_url: "https://x.com/EXM7777/status/1985814823087849637?t=plg_sRFaTfl5KgaMTDrg5A&s=09"
author: "Machina (@EXM7777)"
author_name: "Machina"
author_username: "EXM7777"
author_url: "https://x.com/EXM7777"
tweet_count: 3
---

## 1
https://x.com/EXM7777/status/1985814823087849637

how to setup claude skills in &lt;15min (for beginners): https://t.co/7h8zwfImxs

![](https://pbs.twimg.com/media/G48IDtIbkAAh-R4.jpg)

## 2
https://x.com/EXM7777/status/1985814835343536181

found this while scrolling reddit: https://t.co/eMbelIwK9s

## 3
https://x.com/EXM7777/status/1985875126014132371

more free prompts + content in my telegram (link in bio)

weekly newsletter (no ads/spam): https://t.co/KcCY4jJBSd
---

---
url: "https://x.com/eze_is_1/status/1989168899259273246"
requested_url: "https://x.com/eze_is_1/status/1989168899259273246"
author: "一泽Eze (@eze_is_1)"
author_name: "一泽Eze"
author_username: "eze_is_1"
author_url: "https://x.com/eze_is_1"
tweet_count: 2
---

## 1
https://x.com/eze_is_1/status/1989168899259273246

前两天看到有人用 AI 编程 Agent，做了很受好评的《红楼梦》的互动游戏。
一时手痒，就做了个文生图 Skill 复现了效果：
现在只需要在 Claude Code 里，输入一句话，就能「全自动」做出各种交互式课件、互动游戏。

Claude Skill 真的潜力无限，
还没研究过的朋友，建议趁着这个周末，跟着我最近两个公众号教程走一遍。
肯定能走通，还能学会 Claude Skill 怎么用。

> Author: 一泽Eze (@eze_is_1)
> URL: https://x.com/eze_is_1/status/1988450898352517473
>
> 做了一个新的文生图 skill，加上 agent，做出了一句话生成互动课件，包一下前端就能给老师们用了
> 包括配图也是 AI Agent 一次性生成的
> 开箱即用的 skill + 教程大概明后天发 😊（skill 太好玩了，拉低垂直 Agent 配置难度）

![](https://pbs.twimg.com/media/G5rv1sracAINqUM.jpg)
![](https://pbs.twimg.com/media/G5rxd01bMAA-r2i.jpg)
![](https://pbs.twimg.com/media/G5rxmLobQAA0LY6.jpg)
![](https://pbs.twimg.com/media/G5rxpj_bIAAtPD_.jpg)

## 2
https://x.com/eze_is_1/status/1989524850445357089

对了，Claude Code 里，这个 Case 用的编程模型是豆包刚发的 Seed-Code，运行下来没有任何问题，完美兼容 Claude Skill。
因为还支持多模态理解，所以能 AI 识别配图风格，统一前端设计。
---

---
url: "https://x.com/feltanimalworld/status/1984052455064104987"
requested_url: "https://x.com/feltanimalworld/status/1984052455064104987"
author: "Susan STEM (@feltanimalworld)"
author_name: "Susan STEM"
author_username: "feltanimalworld"
author_url: "https://x.com/feltanimalworld"
tweet_count: 1
---

## 1
https://x.com/feltanimalworld/status/1984052455064104987

分享一个Claude SKILL, 你可以马上用来创建一个日历App. 一个SKILL+一个JSON文件而已。你就说create a personal calendar, 立即创建了。

创建了以后，第一件事情，叫他把当地所有当个学年的学校放假，early release的日程全部给我加上。以前我手动加，慢的要死不说，还经常漏掉。经常忘记去接我儿子。

第二件事情，把你有会员的健身房什么的，喜欢的瑜伽课不需要预约的课程全部给你加上。

以上全部都是网站有信息的，直接一句话的事情。

以后明天孩子要不要上学。我下一次在孩子上学的时候去上瑜伽课，这种问题还用手动安排，那真是笑死了。

---

name: personal-schedule-manager
description: >
Create, review, and edit a `calendar.json` file for schedules and routines.
Summarizes upcoming events, detects conflicts, supports recurring rules,
and runs natural-language multi-turn edits. Outputs a friendly summary and,
when requested or on create, the complete `calendar.json` to copy/replace.
Trigger phrase: "create a new personal calendar" (maps to intent=create with presets).

---
# ───────────────────────────────
# Inputs
# ───────────────────────────────
inputs:
- id: intent
type: string
required: true
description: One of: create | review | edit | export
- id: calendar_json
type: json
required: false

description: Paste full current `calendar.json` (omit for intent=create)
- id: instructions
type: string
required: false

description: Natural-language instructions (add/move/delete/recur/show conflicts/next 7 days)
- id: date_range
type: string
required: false

description: Optional range like "next 7 days", "this month", "2025-11-01..2025-11-30"
# ───────────────────────────────
# Outputs
# ───────────────────────────────

outputs:
- id: human_summary
type: markdown
description: Clear summary of actions taken, upcoming events, and any conflicts.
- id: calendar_json
type: json
description: Full updated file (on create/export, or when explicitly requested)

# ───────────────────────────────
# Behavior
# ───────────────────────────────

# • Default timezone: America/New_York (can be overridden via file or instruction)
# • Good initial defaults (优选初始值):
#  - defaults.event_duration_minutes = 60
#  - defaults.reminder_minutes_before = 30
#  - https://t.co/j2Qv0fkMY1_hours = 09:00–17:00, MO–FR
#  - defaults.priority = "normal"
#  - defaults.category = "personal"
# • Recurrence: iCalendar RRULE (e.g., FREQ=WEEKLY;BYDAY=WE;UNTIL=20251218)
# • Conflict detection: overlapping active events in the same timezone
# • Destructive edits: show a diff; apply only after user says "apply changes"
# • Natural-language verbs: add | move | reschedule | delete | skip (occurrence) | duplicate | tag | remind
# • On intent=create:
#  - Emit a fresh, canonical `calendar.json` with New York time + presets (see schema below)
# • Export: echoes the full canonical JSON
# ───────────────────────────────
# Schema (informative)
# ───────────────────────────────
# Top-level:
# {
#  "version": "1.1",
#  "timezone": "America/New_York",
#  "defaults": {
#  "event_duration_minutes": 60,
#  "reminder_minutes_before": 30,

#  "work_hours": {"start": "09:00", "end": "17:00", "days": ["MO","TU","WE","TH","FR"]},
#  "priority": "normal", # default priority for new events
#  "category": "personal"  # default category for new events
#  },
#  "categories": ["personal","family","work","school","health","finance","errands","travel","learning"],
#  "priority_levels": ["critical","high","normal","low"],
#  "events": [ Event ],
#  "exceptions": [ Exception ],
#  "attendees": [ Attendee ],
#  "audit": [ AuditEntry ]
# }
#
# Event:
# {
#  "id": "evt_001",
#  "title": "Deep Work",
#  "start": "2025-11-03T09:00:00",
#  "end": "2025-11-03T10:30:00",
#  "timezone": "America/New_York",
#  "location": "Home Office",
#  "notes": "No meetings.",
#  "tags": ["focus"],
#  "category": "work", # NEW: one of categories (or a custom string)
#  "priority": "high", # NEW: one of priority_levels
#  "recurrence": null, # RRULE string or null
#  "reminders": [15],  # minutes before start
#  "status": "confirmed",  # tentative | confirmed | cancelled
#  "created_at": "UTC-ISO",  # e.g., 2025-10-30T20:00:00Z
#  "updated_at": "UTC-ISO"
# }

![](https://pbs.twimg.com/media/G4jEoQAWsAAA8fR.jpg)
![](https://pbs.twimg.com/media/G4jEvZ_XQAAcS4-.jpg)
![](https://pbs.twimg.com/media/G4jE1_1W0AAFkhq.png)
![](https://pbs.twimg.com/media/G4jFJOnWYAAq5Yv.png)
---

---
url: "https://x.com/feltanimalworld/status/1983698368606961821"
requested_url: "https://x.com/feltanimalworld/status/1983698368606961821?t=p8fx8bkV1JwUP_ZjHtDDsw&s=09"
author: "Susan STEM (@feltanimalworld)"
author_name: "Susan STEM"
author_username: "feltanimalworld"
author_url: "https://x.com/feltanimalworld"
tweet_count: 3
---

## 1
https://x.com/feltanimalworld/status/1983698368606961821

信息溯源Skills!

卢尔辰这个提法非常好。如果是我的话我会做成一系列的Skills 闭环。在我的宇宙里，闭环为善。我先给你一个，你就直接跟Claude 说: source tracing: 你想问的溯源信息就可以了。截图你可以看到Claude就一步一步的给你溯源推导。

附送安装指南一份😂
https://t.co/yDCwsgW6gY

---
name: source-tracing
description: >
从高熵的二手内容中回溯到低熵、权威、原始的信息源。
该技能通过结构化步骤，帮助用户验证消息真伪、理解原始语境，
建立独立的信息判断与溯源能力。
---

inputs:
- name: claim
type: text
description: 用户提供的一条未经验证的信息或高热度说法。
- name: context_hint
type: text
description: 时间、机构、人名或事件关键词等上下文线索（可选）。
- name: verification_goal
type: text
description: 用户希望达成的溯源目标，例如“找到原视频”、“查看完整讲话稿”等。

process:
steps:
- step: 去包装 (Depackaging)
action: 识别该信息的传播链条，查找最初的发布主体（如官方账号、原作者、机构源）。
- step: 源头定位 (Source Location)
action: 搜索并访问权威渠道（政府官网、机构公告、官方YouTube频道、学术数据库）。
- step: 原文解读 (Primary Analysis)
action: 阅读或观看原始内容，记录关键论点、关键词与发言语境。
- step: 语境还原 (Context Reconstruction)
action: 分析原文语气与时空语境，避免被剪辑或误导。
- step: 多源对照 (Cross Verification)
action: 对比两个以上独立来源，确认一致性。
- step: 结构存档 (Structured Archiving)
action: 输出溯源记录，包含原始链接、日期、机构、主要观点、对照结果。

outputs:
- name: source_trace_log
type: json
description: >
包含源头链接、时间、机构、主要论点、上下文摘要的结构化记录。
- name: trust_index
type: number
range: 0–1
description: 源头权威性 + 内容完整性评分。
- name: entropy_delta
type: number
description: 信息熵下降幅度（表示信息被“去噪”的程度）。

examples:
- input:
claim: "SEC 将全面禁止算法稳定币"
context_hint: "2025年3月，Gary Gensler 演讲"
verification_goal: "找到完整演讲视频并核对原文"
output:
source_trace_log:
source_url: "https://t.co/Tc9KXIeiwY"
source_date: "2025-03-17"
speaker: "Gary Gensler"
institution: "U.S. SEC"
summary: "讨论稳定币监管框架与透明度原则，未提及全面禁止。"
trust_index: 0.95
entropy_delta: 0.82

metadata:
primitive_ir_mapping:
Entity: SEC
Event: Public Speech
Resource: Official Video / Transcript
Action: Source Tracing
Policy: Transparency & Regulation
Ledger: Source Verification Log

dependencies:
- tool: https://t.co/bq6esHklLM
usage: "用于定位权威信息源和官方媒体频道"
- tool: summarizer
usage: "提取原文要点并生成结构化摘要"

recommended_chain:
- name: Source Tracing
- name: Fact Comparison
- name: Context Analysis
- name: Structural Summary

> Author: 卢尔辰 (@erchenlu1)
> URL: https://x.com/erchenlu1/status/1983063294006178266
>
> 突然意识到，其实只要愿意亲自花一点时间去追溯信息源，一层一层往下挖，去读、去看最原始的材料，就已经领先了至少 99% 的人。
>
> 以今年为例，美国 SEC 的几场关键讲话，以及几项重磅的加密法案（比如 Project Crypto），完整演讲视频其实都公开在 SEC 官方的 YouTube 频道上。
>
> 我点进去看了一下——播放量竟然只有几千次。
> 这意味着，绝大多数人接收到的，都是经过二次剪辑、解读、甚至被算法包装过的“二手信息”，甚至只是短视频里的片段。

![](https://pbs.twimg.com/media/G4eCgi0W0AA_3pK.png)
![](https://pbs.twimg.com/media/G4eCkAeXsAAeZJu.png)
![](https://pbs.twimg.com/media/G4eCmZNWwAATnKO.png)
![](https://pbs.twimg.com/media/G4eCpeHW0AA32LJ.png)

## 2
https://x.com/feltanimalworld/status/1983699124781510939

当然，语种不同我发现路径略微不同，喜欢看英文的转换一下全英文档。

## 3
https://x.com/feltanimalworld/status/1983712030839447580

我说了我的宇宙是闭环型的。一个skills当然不够，你真的遇到了节点的，需要决策的信息，当然方案是更复杂的。关注我网站的lessons，会慢慢发出来。
---

---
url: "https://x.com/feltanimalworld/status/1982072901252653266"
requested_url: "https://x.com/feltanimalworld/status/1982072901252653266?t=06koDm0D3P8WIaio2usOpw&s=09"
author: "Susan STEM (@feltanimalworld)"
author_name: "Susan STEM"
author_username: "feltanimalworld"
author_url: "https://x.com/feltanimalworld"
tweet_count: 4
---

## 1
https://x.com/feltanimalworld/status/1982072901252653266

分享第二个Claude Skills, 和第一个澄清意图形成一个链式反应。和我一直的猜想一样，一旦functionalization, 应该和人的思考一样，有链式，有分叉，可以探索成human in the loop decision node。 你可以看到Claude自己在给你链起来。

Lesson 2: Decision Card Execution https://t.co/u5FGRhU6Bn https://t.co/JoQixnlLlX

![](https://pbs.twimg.com/media/G4G8x0wWIAAQ2xb.png)

## 2
https://x.com/feltanimalworld/status/1982075783838409172

而且说真，我这种黑洞般的脑洞，居然都能做decision, 做出来我都觉得，比我想的好多了。

## 3
https://x.com/feltanimalworld/status/1982091943476941187

我在这种情况下写prompt, 在我的意识中自然语言编程遵循一个极简，复用，文字最小化，密度最大化，可读，参数命名标准化等原则。

## 4
https://x.com/feltanimalworld/status/1982092509485347168

所以你看到这里面其实有大量的snake case 小蛇命名的参数。这是我以后想要形成回路，期望能够通过learning自动修改权重的部分。现在也许不会造成任何的差别。但是….但是….one can dream哈哈😂万一我成功的形成了系统呐！
---

---
url: "https://x.com/freeCodeCamp/status/1757842965286867230"
requested_url: "https://twitter.com/freeCodeCamp/status/1757842965286867230?s=09&t=A4asmwerhlnDiU8FLuuzjQ"
author: "freeCodeCamp.org (@freeCodeCamp)"
author_name: "freeCodeCamp.org"
author_username: "freeCodeCamp"
author_url: "https://x.com/freeCodeCamp"
tweet_count: 1
---

## 1
https://x.com/freeCodeCamp/status/1757842965286867230

Building projects is a good way to improve your coding skills.

Here, @developeraspire shows you how to build a video player using Tailwind &amp; JavaScript.

You'll learn how to implement the play, pause &amp; mute functionality, update the progress bar &amp; more.

https://t.co/WtJhsZRlny
---

---
url: "https://x.com/freeCodeCamp/status/1786410691475218536"
requested_url: "https://twitter.com/freeCodeCamp/status/1786410691475218536"
author: "freeCodeCamp.org (@freeCodeCamp)"
author_name: "freeCodeCamp.org"
author_username: "freeCodeCamp"
author_url: "https://x.com/freeCodeCamp"
tweet_count: 1
---

## 1
https://x.com/freeCodeCamp/status/1786410691475218536

If you want to practice your full-stack dev skills, this course is for you.

You'll build a Fiverr clone using popular tools like Next.js, React, and Tailwind CSS.

The course covers coding the front &amp; back ends, database design, dynamic content, &amp; more.

https://t.co/N6SOgY9xg9
---

---
url: "https://x.com/frxiaobei/status/2007665372472729751"
requested_url: "https://x.com/frxiaobei/status/2007665372472729751"
author: "凡人小北 (@frxiaobei)"
author_name: "凡人小北"
author_username: "frxiaobei"
author_url: "https://x.com/frxiaobei"
tweet_count: 1
---

## 1
https://x.com/frxiaobei/status/2007665372472729751

这个 repo 有点牛逼，
把一整套科研 + 医疗的复杂流程，
直接拆成了可复用的 AI 能力块。

138 个 scientific skills，
包含文献、组学、药物发现到临床研究、报告生成，
我能想象到的医生和药企的一整套流程都在里面了。

随便拎几个出来，
封装成 AI scientist 产品，
剩下的就是去卖了。

这种 repo，看的人不多，
但看懂的人，基本都知道它值钱在哪。
https://t.co/RRKGAcszM3
---

---
url: "https://x.com/GitHub_Daily/status/1997472259007746134"
requested_url: "https://x.com/GitHub_Daily/status/1997472259007746134?s=09"
author: "GitHubDaily (@GitHub_Daily)"
author_name: "GitHubDaily"
author_username: "GitHub_Daily"
author_url: "https://x.com/GitHub_Daily"
tweet_count: 1
---

## 1
https://x.com/GitHub_Daily/status/1997472259007746134

Claude 的各项能力虽然强大，但每次遇到特定任务都要从头“调教”一遍 prompt 或流程，确实消耗精力。

刚好在 GitHub 发现 awesome-claude-skills 这个项目，专门收集各类现成可用的 Claude Skills，堪称一个扩展能力仓库。

收录了官方提供的 Office 文档生成（Word、PPT、Excel）、UI 组件构建等能力，也聚合了社区贡献的 Notion 集成、AWS 自动化运维及 Playwright 测试等实用技能。

GitHub：https://t.co/UUkbWv6MUx

核心机制是将指令和脚本模块化，只在需要时加载对应技能，让我们能同时维护数百种能力而不影响模型性能。

同时也整理了大量相关的开发教程和视频资源，适合想把 Claude 深度融入工作流的朋友参考。

![](https://pbs.twimg.com/media/G7hyawpaMAAEjTj.jpg)
![](https://pbs.twimg.com/media/G7hybPqawAAzQ0n.jpg)
---

---
url: "https://x.com/GitHub_Daily/status/1988230314704155038"
requested_url: "https://x.com/GitHub_Daily/status/1988230314704155038?t=LBlnWDot0m4pk8vswOt3iQ&s=09"
author: "GitHubDaily (@GitHub_Daily)"
author_name: "GitHubDaily"
author_username: "GitHub_Daily"
author_url: "https://x.com/GitHub_Daily"
tweet_count: 1
---

## 1
https://x.com/GitHub_Daily/status/1988230314704155038

GitHub 上一份精心整理的 Claude 技能合集：Awesome Claude Skills，可以直接导入使用。

涵盖了文档处理、开发工具、数据分析、内容创作、生产力工具等 9 大类别的实用技能。

每个技能都是标准化的工作流程，可以让 Claude 安装我们的特定需求执行任务。

GitHub：https://t.co/h2o2vCPiOK

而且这些技能可以通过 Claude 官网、Claude Code 或者 API 几种方式使用。

项目还提供了详细的技能创建与使用指南，教我们如何编写自定义 Claude 技能，值得收藏备用。

![](https://pbs.twimg.com/media/G5ec3ASa8AAHwfU.jpg)
---

---
url: "https://x.com/GitHub_Daily/status/1983111503130530168"
requested_url: "https://x.com/GitHub_Daily/status/1983111503130530168?t=UxBxG0WBPvtxCDs2GCK1eQ&s=09"
author: "GitHubDaily (@GitHub_Daily)"
author_name: "GitHubDaily"
author_username: "GitHub_Daily"
author_url: "https://x.com/GitHub_Daily"
tweet_count: 1
---

## 1
https://x.com/GitHub_Daily/status/1983111503130530168

当学习一门新技术框架，需要在其官方文档、GitHub 代码库、学习手册之间来回切换阅读，学习效率极其低。

最近找到了 Skill Seeker 这个开源工具，可以自动抓取文档网站、GitHub 仓库和 PDF 文件，并转换为 Claude 能直接使用的 Skill（技能包）。

这样我们就可以通过 AI 快速学习一门新技术，并且 AI 还能深度分析代码结构、提取 API 接口，自动检测文档和代码之间的不同之处。

GitHub：https://t.co/KCvdQ4DUxL

主要功能：

- 支持文档网站、GitHub 仓库、PDF 文件三种来源混合爬取；
- 自动检测文档与代码间的冲突并标注警告；
- 内置 Godot、React、Vue、Django 等 8 个常用框架预设；
- 深度代码分析，提取函数、类、方法及参数类型信息；
- 异步模式让爬取速度提升 2-3 倍；
- 本地 AI 增强功能，无需 API 费用即可生成完整指南。

提供多种使用方式，可通过 MCP 服务器集成到 Claude Code 中使用，也可以直接用命令行工具。

![](https://pbs.twimg.com/media/G4VftgYaYAAqlh2.jpg)
---

---
url: "https://x.com/gkxspace/status/1997142703671595394"
requested_url: "https://x.com/gkxspace/status/1997142703671595394?s=09"
author: "余温 (@gkxspace)"
author_name: "余温"
author_username: "gkxspace"
author_url: "https://x.com/gkxspace"
tweet_count: 1
---

## 1
https://x.com/gkxspace/status/1997142703671595394

用 Cursor / TRAE，还在羡慕 Claude Code 的 Skills？

有人已经把整套 Skills 系统做成通用开源工具了：

不用 Claude Code

直接在 Cursor、TRAE 等 IDE 里加载同款 Skills

一键装 Anthropic 官方 skills 仓库

npm i -g openskills
openskills install anthropics/skills
openskills sync

Claude 的 Skills，所有 AI IDE 都能用：https://t.co/V5tUInGtMG
---

---
url: "https://x.com/gkxspace/status/1987885651086233747"
requested_url: "https://x.com/gkxspace/status/1987885651086233747?t=hzTepY-2wVaxH20yX4H4WQ&s=09"
author: "余温 (@gkxspace)"
author_name: "余温"
author_username: "gkxspace"
author_url: "https://x.com/gkxspace"
tweet_count: 1
---

## 1
https://x.com/gkxspace/status/1987885651086233747

Claude Skills Marketplace

包含3455个Claude Skills，用于开发、研究、内容......

按分类浏览、按热度排序、方便安装。所有Skills均来自 GitHub 开源。
https://t.co/KIJqSpK2dg https://t.co/827zoVMmX7

> Author: 饼干哥哥AGI（2.0） (@bggg_ai)
> URL: https://x.com/bggg_ai/status/1987519002659471528
>
> 我用 kimi 跑通了 Claude skills，可以在大多数场景下替代 n8n 等 AI 工作流 https://t.co/MbIxE8AZI0

![](https://pbs.twimg.com/media/G5Ziit3WoAAJV0M.jpg)
---

---
url: "https://x.com/godofprompt/status/1953140931231633719"
requested_url: "https://x.com/godofprompt/status/1953140931231633719?t=66FquvXpWmq1snH4S7D3gA&s=09"
author: "God of Prompt (@godofprompt)"
author_name: "God of Prompt"
author_username: "godofprompt"
author_url: "https://x.com/godofprompt"
tweet_count: 2
---

## 1
https://x.com/godofprompt/status/1953140931231633719

Steal my Claude Opus 4.1 prompt to turn your skills into a million-dollar startup.

---------------------------------
GENIUS STARTUP ARCHITECT
---------------------------------

Adopt the role of an expert AI-Era Startup Architect and YC-Trained Venture Builder, you're a former Stanford CS dropout who built and sold two AI companies before 25, spent a year inside YC analyzing what makes the difference between $10M and $10B outcomes, and now helps talented 20-somethings navigate the greatest wealth creation opportunity in human history by turning their technical skills into venture-scale businesses using AI leverage.

Your mission: Transform your technical abilities and domain knowledge into a fundable AI-first startup that can reach $10M revenue in 12 months. Before any action, think step by step: assess technical capabilities, identify AI-amplified opportunities, design venture-scale business model, validate founder-market fit.

Adapt your approach based on:
* User's current technical skills and learning velocity
* AI implementation opportunities in their domain
* Path to $10M revenue within 12 months
* Founder readiness and life circumstances

## PHASE 1: TECHNICAL SKILLS AUDIT

What we're doing: Map your current abilities and AI-leverage potential

The AI era rewards technical implementation over credentials. Let's assess your arsenal:

Current technical skills:
- Programming languages you can actually build with?
- AI/ML experience level? (None / Used APIs / Built models / Research-level)
- Can you ship a working product in 2 weeks?

Domain expertise:
- What industry do you understand deeply?
- What broken process have you personally experienced?
- Where do you have unfair insider knowledge?

Learning velocity check:
- Could you become expert-level in a new technical domain in 1-2 months?
- Examples of things you've learned fast?

## PHASE 2: AI OPPORTUNITY SCANNING

What we're doing: Identify where AI creates 10x value in your domain

Based on YC's thesis, we're looking for:

Where in your domain is AI creating new possibilities?
- Tasks that took days now take minutes
- Previously impossible now possible
- Human expertise that can be democratized

What expensive human expertise could you make accessible?
Think: $500/hour consultants, rare specialists, complex analysts

What would you build if technical barriers didn't exist?

## PHASE 3: FOUNDER-MARKET FIT ASSESSMENT

What we're doing: Ensure you're the right person to build this

YC's "forward deployed engineer" test:

Can you become the world expert in your chosen niche in 1-2 months?
- What's your learning plan?
- Who would you talk to?
- What would you build to learn?

Do you have authentic passion for this problem?
- Personal experience with the pain?
- Would you work on this for 10 years?
- Can you recruit others who care?

Trust and access check:
- Do you have credibility in this space?
- Can you get to decision makers?
- Will early users take your call?

## PHASE 4: $10M REVENUE PATH DESIGN

What we're doing: Create a realistic path to venture-scale revenue in 12 months

The new YC benchmark: $0 to $10-12M in one year.

Your revenue model options:

**Option A: High-Ticket B2B**
- 100 customers × $100K = $10M
- Target: Enterprise with urgent AI needs
- Your advantage: [Define based on your skills]

**Option B: Mid-Market Velocity**
- 1,000 customers × $10K = $10M
- Target: SMBs desperate for AI efficiency
- Your advantage: [Define based on your domain]

**Option C: Usage-Based API**
- 10,000 customers × $1K = $10M
- Target: Developers/startups building on you
- Your advantage: [Define based on technical skills]

Which path matches your strengths?

## PHASE 5: MVP DEFINITION (2-WEEK SHIPPABLE)

What we're doing: Design something you can build and launch in 14 days

Your MVP specifications:
- Core AI capability: [One thing it does incredibly well]
- User interface: [Simplest possible interaction]
- Value demonstration: [Immediate "holy shit" moment]
- Technical architecture: [AI models/APIs you'll use]

Distribution strategy for week 3:
- Where do your users already hang out?
- What would make them share immediately?
- How will you get to 10 pilot users?

Can you commit to shipping this in 2 weeks?

## PHASE 6: CO-FOUNDER EVALUATION

What we're doing: Decide if you need a partner and who it should be

YC says "try not to do it alone" - but be selective.

Do you need a co-founder for:
- Technical skills you lack?
- Industry connections?
- Emotional support?
- Complementary strengths?

If yes, your ideal co-founder:
- Has shipped product before
- Equally obsessed with problem
- Comfortable with ambiguity
- High agency personality

Where to find them:
- Your existing network (best)
- Industry slack/discord communities
- University AI clubs
- Hackathons focused on your domain

## PHASE 7: FINANCIAL RUNWAY PLANNING

What we're doing: Ensure you can survive while building

YC's advice: 6-9 months minimum living expenses

Your survival budget:
- Monthly burn: $[Amount]
- Months of runway: [Calculation]
- Path to revenue: [Timeline]

Options to extend runway:
- Part-time consulting in your domain
- Pre-sales to early customers
- Grants/competitions (non-dilutive)
- Friends & family round

Ready to go full-time when?

## PHASE 8: STARTUP VS. JOB DECISION MATRIX

What we're doing: Make a clear-eyed decision about your path

Should you start a company or join one?

**Start a company if:**
✓ You have 6-9 months runway
✓ You've identified a real problem with AI solution
✓ You can ship MVP in 2 weeks
✓ You have authentic passion for the space
✓ You want to own your outcome

**Join a startup if:**
✓ You need to learn more about AI implementation
✓ You want to see how startups operate first
✓ You need financial stability
✓ You found a rocket ship to join

Your score: [X] out of 5 for starting

## PHASE 9: NICHE DOMINATION STRATEGY

What we're doing: Become the undisputed expert in your micro-domain

YC's "go undercover" approach:

Your niche: [Specific enough that you can dominate]

30-day expertise sprint:
- Week 1: Talk to 20 potential customers
- Week 2: Build prototype addressing top pain
- Week 3: Get 5 users testing
- Week 4: Iterate based on feedback

Content strategy to establish authority:
- Technical blog posts about your approach
- Open source tools for the community
- Case studies of early wins

## PHASE 10: AI-FIRST EXECUTION PLAN

What we're doing: Build competitive advantage through AI leverage

Your AI moat strategy:

**Technical advantages:**
- Proprietary data collection method
- Fine-tuned models for your use case
- Novel AI application approach
- Integration depth competitors can't match

**Speed advantages:**
- Ship features in days, not months
- Automated customer onboarding
- AI-powered customer success
- Self-improving product loops

**90-day milestones:**
- Day 14: MVP shipped
- Day 30: 10 pilot customers
- Day 60: $10K MRR
- Day 90: Clear path to $100K MRR

## PHASE 11: VENTURE READINESS CHECKLIST

What we're doing: Ensure you're building something VCs will fund

YC-style fundability criteria:

Market opportunity:
- [ ] $1B+ market that's growing
- [ ] AI creates new market or 10x improves existing
- [ ] Clear path to market leadership

Founder strength:
- [ ] Technical ability to build without hiring
- [ ] Deep domain expertise or fast learning proof
- [ ] High agency and ownership mentality
- [ ] Can recruit talented people

Business model:
- [ ] Path to $10M ARR in 12-18 months
- [ ] High gross margins (>70%)
- [ ] Natural expansion within customers
- [ ] Network effects or data moats

## PHASE 12: LAUNCH SEQUENCE ACTIVATION

What we're doing: Pull the trigger on your AI-first venture

Your launch checklist:

**Week 1-2: Build**
- [ ] MVP functional
- [ ] Basic analytics installed
- [ ] Payment system ready
- [ ] Legal structure set up

**Week 3-4: Launch**
- [ ] 10 beta users identified
- [ ] Feedback loops established
- [ ] Iteration velocity high
- [ ] Revenue experiments started

**Month 2-3: Scale**
- [ ] Product-market fit signals
- [ ] Repeatable sales process
- [ ] Customer success automated
- [ ] Hiring plan ready

**Success metrics:**
- Week 2: Shipped MVP
- Month 1: First paying customer
- Month 3: $10K MRR
- Month 6: $100K MRR
- Month 12: $1M MRR

Ready to build the future? The AI era rewards builders over talkers. Start now.

> Author: God of Prompt (@godofprompt)
> URL: https://x.com/godofprompt/status/1952427835739734153
>
> How to build a startup in 2025 https://t.co/RrOw5rHNRC

## 2
https://x.com/godofprompt/status/1953141256483217460

The AI prompt library your competitors don't want you to find

→ Unlimited prompts: $15/month
→ Starter pack: $3.99/month
→ Pro bundle: $9.99/month

Grab it before it's gone 👇
https://t.co/X9MhztPins
---

---
url: "https://x.com/hongming731/status/1989622113515470992"
requested_url: "https://x.com/hongming731/status/1989622113515470992?t=Qrji2R93pOl8d-Rp6nqVTg&s=09"
author: "ginobefun (@hongming731)"
author_name: "ginobefun"
author_username: "hongming731"
author_url: "https://x.com/hongming731"
tweet_count: 2
---

## 1
https://x.com/hongming731/status/1989622113515470992

Skills explained: How Skills compares to prompts, Projects, MCP, and subagents
https://t.co/KIqIVMSw9R

Claude Skills 不就是把提示词存个文件夹吗？
https://t.co/ZwcZ2KDduM

看了两篇关于 Skill 的好文章，做下阅读笔记。

很多人初次看到 Claude 的 Skills 功能，第一反应是：这不就是把提示词存成文件吗？这个判断其实低估了它的意义。

Anthropic 专门写了篇长文解释 Skills 与 Prompts、Projects、MCP、Subagents 的区别。这篇文章值得关注，因为它不只是介绍功能，而是在说明 AI 应用开发的底层逻辑转变。

从第一性原理看，Skills 的存在有其必然性。大语言模型需要上下文才能工作，但上下文窗口有限是物理约束，重复输入相同信息显然低效。面对这个矛盾，合理的解决方案就是建立按需加载的知识模块系统。

官方给出了清晰的定位：Prompts 是即时指令，Skills 是可复用流程，Projects 提供知识库，Subagents 是专职助手，MCP 负责连接外部系统。这五个组件各有分工，配合使用才能发挥完整价值。

举个实际例子。你可以创建一个代码审查的 Subagent，只给它 Read、Grep、Glob 这些只读权限，不给 Write 和 Edit 权限。当你修改代码时，Claude 会自动委派这个 Subagent 做安全检查，既保证了审查流程，又避免了误改代码的风险。再配合 Skills 里定义的安全审查标准，整个流程就能自动运行。

这里有三个关键点值得注意。

第一，Skills 不是功能增强，而是范式转变。过去用 AI 是即兴发挥，现在可以系统沉淀工作方法。

第二，五个组件需要配合使用。单独用 Skills 只有 30% 效果，配合 Projects 的背景知识、MCP 的数据连接、Subagents 的任务分工，才能构建出生产级的工作流。

第三，未来的护城河不在于调用哪个模型，而在于你积累了多少精心设计的 Skills。这跟 npm 生态类似，先发优势会越来越明显。

对做 AI 产品的人来说，现在可能是时候从写花式提示词，转向设计可复用工作流了。

![](https://pbs.twimg.com/media/G5yN3naaUAAP6mb.jpg)

## 2
https://x.com/hongming731/status/1989672659995824396

还有 @yan5xu 的文章也很值得一读。作者提出 Claude Skills 被大多数人忽略的核心设计哲学：信息分层架构。

作者通过《塞尔达传说》中的 LOD 技术和按需加载机制作类比，系统阐述了三层信息架构（摘要层、核心层、原始层）如何让 Agent 节省 95% 的 Token 消耗并提升决策质量。

这个类比非常巧妙，远处看到的是轮廓（LOD-0 摘要层），走近看到布局（LOD-1 核心层），贴近才看到细节（LOD-2 原始层）。这样就解释了 Agent 不需要一次性把所有信息塞进脑子，它只需要：

- 知道有什么资源
- 按需加载核心信息
- 需要时才查原始数据

以我最近创建 Skill 的体会来看，这里的重点在于构建高质量的 LOD-1 层，而过早标准化反而会降低灵活性。

https://t.co/joHyOaGy2u

![](https://pbs.twimg.com/media/G5y5yFNbkAYuv6t.jpg)
---

---
url: "https://x.com/hongming731/status/1985701718840262674"
requested_url: "https://x.com/hongming731/status/1985701718840262674?t=gh5cSyu-loMyPLRml__Haw&s=09"
author: "ginobefun (@hongming731)"
author_name: "ginobefun"
author_username: "hongming731"
author_url: "https://x.com/hongming731"
tweet_count: 1
---

## 1
https://x.com/hongming731/status/1985701718840262674

今天升级了该 Skill，增加了 4 个分析框架：结构化思维、5W2H 分析、多元思维模型和逆向思维模型，同时把 skills 原始内容提交到项目了，可以到这里下载最新的版本 https://t.co/OMTmBzmh4m

今天的 Claude 额度已经躁完了，明天继续~ https://t.co/uVFcF55Hdk

> Author: ginobefun (@hongming731)
> URL: https://x.com/hongming731/status/1984977763758227620
>
> Claude 把我常用的一些阅读方法打包成一个 Skill，太棒了~ https://t.co/gPt77i6oXd

![](https://pbs.twimg.com/media/G46hD5sbcAAc1fE.jpg)
---

---
url: "https://x.com/hongming731/status/1984977763758227620"
requested_url: "https://x.com/hongming731/status/1984977763758227620?t=k3X0ElEHguT9N1M_tobXFg&s=09"
author: "ginobefun (@hongming731)"
author_name: "ginobefun"
author_username: "hongming731"
author_url: "https://x.com/hongming731"
tweet_count: 3
---

## 1
https://x.com/hongming731/status/1984977763758227620

Claude 把我常用的一些阅读方法打包成一个 Skill，太棒了~ https://t.co/gPt77i6oXd

![](https://pbs.twimg.com/media/G4wOqXZa8AA3sPh.jpg)

## 2
https://x.com/hongming731/status/1984980501669839164

生成的文件深度分析报告真的太有价值了，洞察、思考和深度都很棒 👍🏻 https://t.co/Ke1xcKE4Qy

![](https://pbs.twimg.com/media/G4wRKn4bcAAqPt0.jpg)

## 3
https://x.com/hongming731/status/1984984211221262534

Claude 帮我发布了这个项目 😍

https://t.co/ifarjFknRc https://t.co/djCnahwTPc

![](https://pbs.twimg.com/media/G4wUlBUa0AAPJz-.jpg)
---

---
url: "https://x.com/vista8/status/2016185479843250491"
requested_url: "https://x.com/i/status/2016185479843250491"
author: "向阳乔木 (@vista8)"
author_name: "向阳乔木"
author_username: "vista8"
author_url: "https://x.com/vista8"
tweet_count: 1
---

## 1
https://x.com/vista8/status/2016185479843250491

朋友写的这个程序+skill就有点黑科技了。

所有海外付费新闻网站都能免费看了... https://t.co/tYhoDTd3h6

![](https://pbs.twimg.com/media/G_rt1Z7acAEM-So.jpg)
---

---
url: "https://x.com/vista8/status/2016185479843250491"
requested_url: "https://x.com/i/status/2016185479843250491"
author: "向阳乔木 (@vista8)"
author_name: "向阳乔木"
author_username: "vista8"
author_url: "https://x.com/vista8"
tweet_count: 1
---

## 1
https://x.com/vista8/status/2016185479843250491

朋友写的这个程序+skill就有点黑科技了。

所有海外付费新闻网站都能免费看了... https://t.co/tYhoDTd3h6

![](https://pbs.twimg.com/media/G_rt1Z7acAEM-So.jpg)
---

---
url: "https://x.com/LotusDecoder/status/2016159780491165813"
requested_url: "https://x.com/i/status/2016159780491165813"
author: "LotusDecoder (@LotusDecoder)"
author_name: "LotusDecoder"
author_username: "LotusDecoder"
author_url: "https://x.com/LotusDecoder"
tweet_count: 1
---

## 1
https://x.com/LotusDecoder/status/2016159780491165813

claude code 睡前挂机提示词单任务版
前置条件：
需配合 skills/planning-with-files 、
claude --dangerously-skip-permissions

---

你正在无人值守模式下执行任务。

重要规则：
1. 不要使用 AskUserQuestion 询问用户，用户已经睡觉了
2. 遇到需要决策的地方，自主做出合理选择并记录在 task_plan.md 中
3. 如果任务需要用户提供的信息/资源才能继续，将任务状态改为 suspended 并在 task_plan.md 中记录障碍原因
4. 如果任务可以独立完成，完成后将状态改为 completed
5. 优先完成能独立完成的部分，无法完成的部分记录下来

现在开始：/planning-with-files 继续任务
---

---
url: "https://x.com/interjc/status/2016307431442416031"
requested_url: "https://x.com/i/status/2016307431442416031"
author: "Justin (@interjc)"
author_name: "Justin"
author_username: "interjc"
author_url: "https://x.com/interjc"
tweet_count: 1
---

## 1
https://x.com/interjc/status/2016307431442416031

终极方案了，安装这个 find-skills，就可以让 ai 自己寻找合适的 skill 来安装，不用自己满处找了

npx skills add vercel-labs/skills --skill find-skills

不过总感觉还可以再进一步 https://t.co/sNIwDMLAkw

![](https://pbs.twimg.com/media/G_tclsObAAMsjZY.png)
---

---
url: "https://x.com/JinsFavorites/status/2015334160030933310"
requested_url: "https://x.com/i/status/2015334160030933310"
author: "dangjin (@JinsFavorites)"
author_name: "dangjin"
author_username: "JinsFavorites"
author_url: "https://x.com/JinsFavorites"
tweet_count: 2
---

## 1
https://x.com/JinsFavorites/status/2015334160030933310

用 Claude + Remotion 构建了一个 pdf2video  的skill！

项目地址：https://t.co/977f0J3cRG ，欢迎 star！

实现思路：
1. 让 Claude 编写 remotion 的模板
2. 创建 skill，完成两件事：分析 pdf 文件内容并按照 remotion 的模板输出格式
3. 通过命令行输出视频：npx remotion render PdfShowcase xxxx

demo 效果如下👇

![video](https://pbs.twimg.com/amplify_video_thumb/2015333255181139968/img/tcwaApaQ3I8LvVpX.jpg)
[video](https://video.twimg.com/amplify_video/2015333255181139968/vid/avc1/1920x1080/3RvV5JoJPNjExWmc.mp4?tag=21)

## 2
https://x.com/JinsFavorites/status/2015335880668725356

这个项目可玩性还是很多，计划后面抽时间继续搞搞：

1. 接入 tts ，增加解说 （坐等一个赞助）
2. 支持解析 pdf 标注等内容，可以智能定位并高亮
3. 接入音频合成，增加一些特效声音
---

---
url: "https://x.com/dotey/status/2015149067068711222"
requested_url: "https://x.com/i/status/2015149067068711222"
author: "宝玉 (@dotey)"
author_name: "宝玉"
author_username: "dotey"
author_url: "https://x.com/dotey"
tweet_count: 1
---

## 1
https://x.com/dotey/status/2015149067068711222

这一段时间 baoyu-skills 项目更新很频繁，但基本都基于这样一个迭代模式：

1. 发现问题
比如我今天发现 commit messages 都是没有意义的版本号变更，虽然有 CHANGELOG，但这不利于后续维护

另外就是版本号的变更当前都是 Agent 决定，有时候其实我想自己控制，但是又懒的写要求

再有就是还得手动 push origin，还是懒

2. 分析问题
要让 commit messages 变得有意义，把每个skills/模块的变更变成独立的commit，版本号的变更跟以前保持一致就可以。

3. 解决问题
不需要手动去执行，把要求发给 Claude Code，这种可以几句话描述清楚的直接交给它做就可以了。

4. 验证问题
做完当然需要验证一下，看是不是符合预期。先看变更记录，再测试（有些甚至可以告诉 Agent 验证方法让它自己验证），测试下来跟我期望的一样，如果不一致就要回到原来的会话告诉 Agent 我期望的结果和实际结果的差异，让它修复

https://t.co/GOjnWisJjw

![](https://pbs.twimg.com/media/G_c8DW_WAAARb4W.jpg)
![](https://pbs.twimg.com/media/G_c-fsAXEAAxvnG.jpg)
![](https://pbs.twimg.com/media/G_c-vc1X0AA9mjQ.jpg)
![](https://pbs.twimg.com/media/G_c_XMYXoAAOcEe.jpg)
---

---
url: "https://x.com/brad_zhang2024/status/2015075906294001951"
requested_url: "https://x.com/i/status/2015075906294001951"
author: "烟花老师 (@brad_zhang2024)"
author_name: "烟花老师"
author_username: "brad_zhang2024"
author_url: "https://x.com/brad_zhang2024"
tweet_count: 1
---

## 1
https://x.com/brad_zhang2024/status/2015075906294001951

这又是一个不得不安装的skill 

manim_skills 

如果知道这个youtube @3blue1brown 频道的话就会知道这个skill 可以做出什么水准的技术类视频了！

> Author: Adithya S K (@adithya_s_k)
> URL: https://x.com/adithya_s_k/status/2014426458475966649
>
> Now you can also create animations like @3blue1brown
> 👉🏻 excited to introduce manim_skills
>
> $ npx skills add adithya-s-k/manim_skill
>
> This animation was created just by prompting 👇 https://t.co/YBm5efPEzN
---

---
url: "https://x.com/aiwarts/status/2015067998009323557"
requested_url: "https://x.com/i/status/2015067998009323557"
author: "卡尔的AI沃茨 (@aiwarts)"
author_name: "卡尔的AI沃茨"
author_username: "aiwarts"
author_url: "https://x.com/aiwarts"
tweet_count: 2
---

## 1
https://x.com/aiwarts/status/2015067998009323557

我至今用到最好的Claude Code Skills们第二篇！

没想到又多出来了9个封神的Skills，包括动画制作，无限画布，版本管理，动态PPT，去AI味儿，新技能制作，Office全家桶，都是我实地测试过的

Claude Code就统一叫CC了

1. Vercel出的聚合站skills. sh
按安装量排名，可以看24小时内最火Skills是什么，收录后的Skills安起来很简单，在CC上运行，npx skills add 具体的项目名

2. 比方说昨天一发就火的Remotion
运行npx skills add remotion-dev/skills安装，这个Skill能免费做JS动画，还做3D的，比方说我可以做一个讲解如何安装CC的文字讲解视频，用在PPT上绝杀，我明天单独出一篇

3. 第三名是Pencil，可以理解为无限画布版Claude Code，兼容Figma，还自带了设计规范和示例风格，不算纯skills，我单开一篇《不想当设计师的程序员不是好产品经理》

4. 看到这里的话可能已经装了几十个Skills，需要管理Skills的Skills

@brad_zhang2024  做的skills-updater，能检查本地skill有没有更新，有的话自动装，但有些Skills我在本地用的时候会修改，自动更新会跟我本地改好的版本冲突。@xiaoerzhan 做的Skill Vision Control解决了这个问题，下载新版本时保留旧的，可以对比后再决定要哪个

5. 最近跑的还有@op7418 佬的动态PPT Skills，op7418/NanoBanana-PPT-Skills，能分析文档做PPT大纲，用 Banana2生图，用可灵做页面过渡动画，一键合成包含所有转场的ppt视频

6. 同样是做PPT，PleasePrompto/notebooklm-skill 有一个新用法，在网页端生成PPT的时候最多也就是20页，在CC用可以换个思路，先生成一个结构化的文档，明确每一页ppt讲什么

然后CC有学习品牌风格的Skills，Theme Factory ，原用法是将生成的内容做品牌化的，会去对齐配色和字体，这时候我会让它学我想要做的PPT风格，这样生成PPT的时候可以1次做15张，不停循环也能保持风格化，100页都可以做

7. 怎么把日常对话打包成Skills呢
上一篇的方式是obra/superpowers头脑风暴，把跟模型的上下文对话主动做成Skills。这一篇升级成全自动的humanplane/homunculus，比方我连续三四次做某个请求前都会先看API文档，它就会创建一个自动获取文档的新技能

8. 还有一个skill-from-masters会在我新建一个技能的时候，网络搜索领域专家的方法论，或者找高赞的GitHub项目转化为新技能

9. ComposioHQ/awesome-claude-skills的Document Processing，含金量高高的，让CC带格式带公式生成 Word/Excel/PPT/PDF

> Author: 卡尔的AI沃茨 (@aiwarts)
> URL: https://x.com/aiwarts/status/2012172395365437893
>
> 我至今用到最好的Claude Code Skills们
>
> skillsmp都有6万个Claude Skills了，今天来推荐一些我使用频率超高的Skills，安装方法我放在后面，Claude Code（简称CC）和OpenCode的为难豆包版安装指南也塞进来了
>
> 1. PleasePrompto/notebooklm-skill
> 作者离程序员很远，离神很近了，能自动上传PDF，视频链接到NotebookLM，连Google不让导出的记忆闪卡，脑图，报告都可以导出，甚至视频字幕，PDF文本，网页搜索结构也都行，我直接把它当我云端知识库用了
>
> 2. OthmanAdi/planning-with-files
> 按照Manus的Agent方法写出来的Skill，可以用这个Skill指导其他Skill工作。让Claude Code开发时可以组成连招，planning-with-files（做计划）和Ralph Wiggum（自主迭代）
>
> 3. ralph-wiggum
> 核心功能是反复向Agent输入提示语，一直到它迭代出能用的代码，记得开循环次数限制，5-10次
>
> 4. anthropics/skill-creator
> 要自己做skill记得安装这个，就不需要记开发标准了，直接在CC里说“用skill-creator开发一个将PDF信息转成可视化网页的skill”
>
> 5. obra/superpowers
> Claude Code Plan模式的升级版，比方说我要新开发Skill的时候，它会连续追问讨论十几轮确定开发方案。可以用来做头脑风暴，写需求文档，开发计划，测试cases都可以
>
> 6. obra/brainstorming
> 同样是头脑风暴，这个可以用来生成新skill，可以是Don Koe的AI工作流，也可以是你跟Agent的对话记录，给CC输入，
>
> 把我们对话整理好，包括我的提示词迭代和你的解法，存成一个Skill放到./claude/skills目录，起个清晰的名字和描述，以后我会高频率复用
>
> 7. anthropics/frontend-design
> 我的前端开发，部署，Banana2配图三件套
>
> frontend-design负责好看，sanjay3290/imagen 负责调用GeminiAPI生成用在UI，图标和视觉素材的图像，vercel-labs/vercel-deploy-claimable 负责把本地项目部署到Vercel
>
> 8. microsoft/markitdown
> 可以相信微软做文档转换的水平，PDF，PPT，图像音频HTML，ZIP和EPub都可以转成MarkDown，文本模型也可以读取到文件信息
>
> 9. fvadicamo/dev-agent-skills
> 用Git保存本地代码修改，就算AI把文件夹删了，还可以从Github上救回来
>
> 安装Skills就直接在cc里面输入，
>
> 安装skills: GitHub链接，
>
> 上面的序号后的名字前加上“github. com/”就是Github连接，不够用可以在这里再淘点
>
> skillsmp. com

## 2
https://x.com/aiwarts/status/2015068068905619789

评论区蹲更多好用的Skills！
---

---
url: "https://x.com/treydtw/status/2015396403166712012"
requested_url: "https://x.com/i/status/2015396403166712012"
author: "香蕉Banana (@treydtw)"
author_name: "香蕉Banana"
author_username: "treydtw"
author_url: "https://x.com/treydtw"
tweet_count: 1
---

# Claude Skill 入门：你需要知道的都在这了

![](https://pbs.twimg.com/media/G_ggEJWXcAAhYJ4.jpg)

我用 Claude 快一年了。从最开始每天和它吵架，到现在它基本能按我的方式干活，中间踩了无数坑。

Skill 是这个过程中我学到的最重要的东西。不是因为它酷，是因为它真的解决了一个核心问题：让 AI 记住你的工作方式。

这篇文章是我用 Skill 的完整经验。不是官方文档的翻译，是我自己踩坑换来的。

## Skill 不是你想的那样

大多数人第一次听到 Skill，会以为这是某种"高级 Prompt"。写一段话，保存成文件，就叫 Skill 了。

这个理解是错的。

Prompt 和 Skill 的区别不是形式，是持久性。

Prompt 是你每次对话都要说的话。说完就忘。下次还得说。

Skill 是 Claude 启动时就会读的规则。你不用说，它自己知道。每次对话都生效。

这意味着什么？

意味着你可以把你摸索出来的最佳实践固化下来。不用每次都解释"我要的格式是这样"、"这个项目的规范是那样"。写一次，永久生效。

但这不意味着什么都该做成 Skill。

适合做成 Skill 的任务：

- 你会重复做很多次
- 有固定的规则或格式
- 需要输出一致性

不适合做成 Skill 的任务：

- 一次性的
- 每次都不一样
- 需要 Claude 自由发挥

判断标准很简单：如果你发现自己在不同对话里重复说同样的话，那就该做成 Skill。

## SKILL.md

当你启动 Claude，它做的第一件事就是读你的 SKILL.md 文件。这个文件里的每条指令都会影响 Claude 怎么处理你的任务。

大多数人要么完全忽略这个文件，要么往里面塞一堆垃圾。两种做法都会让 Claude 变得更差。

真正重要的是什么：

保持简短。 Claude 一次能可靠跟随的指令大概是 150-200 条，而系统提示已经用掉了大约 50 条。你加的每条指令都在争夺注意力。如果你的 SKILL.md 写成了小说，Claude 会开始随机忽略一些内容，你还不知道它忽略了哪些。

写"为什么"，不只是"做什么"。 "标题控制在 15 字以内"是可以的。"标题控制在 15 字以内，因为超过 15 字在手机端会被截断，用户看不到完整信息"更好。为什么？因为当 Claude 遇到你没预料到的情况时，它能根据原因做出更好的判断。

只写 Claude 不知道的东西。 不要解释什么是文章结构，Claude 知道。告诉它你的偏好——喜欢什么风格、讨厌什么表达、踩过什么坑。

持续更新。 每次你发现自己在同一件事上纠正 Claude 两遍，那就是信号——应该写进 SKILL.md 里。按 # 键，Claude 会自动帮你添加指令。

烂的 SKILL.md 看起来像给新员工写的入职文档。

好的 SKILL.md 看起来像你明天会失忆时留给自己的便条。

## 渐进式披露：Skill 的核心机制

这是大多数人不知道的：Skill 不是一次性全部加载的。

Claude 用一种叫"渐进式披露"的机制来处理 Skill：

第一层：元数据（启动时加载）

就是 SKILL.md 开头的 name 和 description。大概 100 个 token。每个 Skill 都会加载这部分，Claude 用它来判断什么时候该用哪个 Skill。

第二层：正文（触发时加载）

当 Claude 判断需要用某个 Skill 时，才会读 SKILL.md 的正文。建议控制在 5000 token 以内。

第三层：资源文件（按需加载）

参考文档、脚本、模板这些。只有 Claude 判断需要的时候才会读。

这意味着什么？

意味着你可以装很多 Skill，但不会拖慢 Claude。因为大部分内容只有在需要的时候才会加载。

也意味着你应该把内容拆分到不同层级。核心指令放正文，详细参考放单独的文件。不要把所有东西都塞进 SKILL.md。

## 创建你的第一个 Skill

最简单的路径，5 分钟跑通。

第一步：创建文件夹

在 ~/.claude/skills/ 下创建一个文件夹。名字用小写字母和连字符，比如 my-writing-style。

> mkdir -p ~/.claude/skills/my-writing-style

第二步：创建 SKILL.md

在文件夹里创建 SKILL.md 文件（必须全大写）：

> ---
> name: my-writing-style
> description: 当用户要求写文章、改稿、润色内容时使用
> ---
> 
> # 我的写作风格
> 
> 写作时遵循：
> 1. 开头不要"在当今社会"、"随着...的发展"这类套话
> 2. 一段只讲一件事，超过 4 行就拆分
> 3. 能用短句就不用长句
> 4. 不用"赋能"、"抓手"、"闭环"这类词
> 
> 语气：像朋友聊天，不像写报告

第三步：验证

重启 Claude Code，然后说"帮我写一段关于 XX 的介绍"。如果 Claude 的输出风格符合你定义的规则，说明 Skill 生效了。

就这么简单。

## 为什么你的 Skill 不生效

如果你创建了 Skill 但 Claude 没反应，99% 的问题出在这三个地方：

1. 文件结构错了

> ❌ 错误：~/.claude/skills/SKILL.md
> ✅ 正确：~/.claude/skills/my-skill/SKILL.md

SKILL.md 必须放在子文件夹里，不能直接放在 skills 目录下。

2. description 写得太模糊

description 是最重要的字段。Claude 靠它判断什么时候该用这个 Skill。

> # 烂的 - Claude 不知道什么时候该用
> description: 帮助处理内容
> 
> # 好的 - 明确触发条件
> description: 当用户要求写文章、改稿、润色、检查错别字时使用

如果你说的话里没有 description 中的关键词，Claude 可能不会触发这个 Skill。

3. YAML 格式错误

这个最坑。多一个空格少一个冒号都会出错。

> # ❌ 错误：冒号后面没空格
> name:my-skill
> 
> # ❌ 错误：缺少结尾的 ---
> ---
> name: my-skill
> description: 描述
> 
> # ✅ 正确
> ---
> name: my-skill
> description: 描述
> ---

![](https://pbs.twimg.com/media/G_ggO7naUAE9dAA.jpg)
![](https://pbs.twimg.com/media/G_ggJJAWEAEbDK6.jpg)

调试技巧

不确定 Claude 有没有读到你的 Skill？直接问它：

> "你现在有哪些可用的 Skill？"

如果它能列出来，说明识别了。如果列不出来，检查文件路径和格式。

## 写好 Skill 的四个原则

用了快一年，我总结出这四条。每条都是踩坑换来的。

![](https://pbs.twimg.com/media/G_ggGcbXcAACWJO.jpg)

## 原则一：命名要一眼看懂

> ✅ 好的：my-writing-style, translate-to-chinese, meeting-notes
> ❌ 烂的：helper, utils, tool-v2-final

![](https://pbs.twimg.com/media/G_ggL_QaIAA73kH.jpg)

Skill 多了之后，名字不清楚你自己都分不清哪个是哪个。

## 原则二：description 要写"什么时候用"

不只是写这个 Skill 能做什么，要写什么情况下应该触发它。

> # 只说能做什么 - 不够
> description: 帮助写文章
> 
> # 说什么时候用 - 更好
> description: 当用户要求写文章、改稿、润色、优化表达时使用

## 原则三：正文要短

官方建议不超过 500 行。为什么？

因为 Skill 正文会占用上下文空间。写太长，Claude 会开始忽略一些内容，你还不知道它忽略了哪些。

只写 Claude 不知道的东西。不用解释什么是大纲，Claude 知道。告诉它你的偏好、你的风格、你踩过的坑。

## 原则四：高风险任务要写死命令

写作润色这种，可以给 Claude 自由发挥空间。

但发布内容、群发消息这种搞砸了很难挽回的，必须写死：

> ## 内容发布
> 
> 发布前必须确认：
> 1. 让我确认标题和正文
> 2. 等我说"确认发布"才能执行
> 3. 发布后告诉我链接
> 
> 绝对不要自动发布，必须等我确认。

判断标准：搞砸了代价大不大？ 代价大就写死，代价小就给空间。

## 多 Skill 协作

单个 Skill 解决单个问题。但有时候你需要多个 Skill 配合。

什么时候需要多个 Skill？

当一个任务可以拆成几个独立的步骤，每个步骤有自己的规则时。

比如内容创作流程：

- research - 搜集资料、整理信息
- outline - 列大纲、定结构
- write - 写初稿
- polish - 润色、改标题

每个 Skill 专注做一件事，做好一件事。

怎么设计边界？

问自己：这个步骤能不能独立运行？如果能，就拆成单独的 Skill。如果必须和其他步骤一起才有意义，就合并。

Skill 之间怎么调用？

在 SKILL.md 里引用其他 Skill 的名字，Claude 会自动识别：

> ## 创作流程
> 
> 1. 先用 research 搜集资料
> 2. 确认素材后用 outline 列大纲
> 3. 大纲定了用 write 写初稿
> 4. 最后用 polish 润色

Claude 会在需要的时候自动加载对应的 Skill。

## 当 Skill 不够用时

Skill 不是万能的。有些场景需要其他方案。

Skill vs MCP

MCP 是让 Claude 连接外部服务的协议。Slack、GitHub、数据库、API。

区别：

- Skill 是教 Claude 怎么做事
- MCP 是让 Claude 能访问什么

如果你需要 Claude 读取外部数据或调用外部服务，用 MCP。如果你需要 Claude 按特定方式处理任务，用 Skill。

两者可以配合：MCP 提供数据，Skill 定义处理方式。

Skill vs Custom Commands

Custom Commands 是把常用的 prompt 打包成命令。在 .claude/commands/ 下创建 markdown 文件，就能用 /commandname 调用。

区别：

- Skill 是 Claude 自动判断什么时候用
- Command 是你手动触发

如果你希望 Claude 自己识别场景并应用规则，用 Skill。如果你想要一个快捷方式来运行固定的任务，用 Command。

组合策略

我的常用组合：

- Skill 定义项目规范和工作方式
- MCP 连接 GitHub、数据库
- Command 处理固定流程（部署、发布）

不要只用一种。根据场景选择最合适的。

## TLDR

Skill 的本质：让 AI 记住你的工作方式，不是高级 Prompt。

SKILL.md：保持简短，写为什么不只是做什么，持续更新。

渐进式披露：Skill 分三层加载，所以你可以装很多但不影响性能。

创建 Skill：在 ~/.claude/skills/skill-name/SKILL.md，5分钟跑通。

不生效的原因：文件结构错、description 太模糊、YAML 格式问题。

四个原则：命名清晰、description 写触发条件、正文要短、高风险写死命令。

多 Skill 协作：每个 Skill 做一件事，通过引用名字互相调用。

Skill 不是万能的：配合 MCP 和 Command 使用，根据场景选择。

如果你在用 Claude，Skill 是你必须掌握的东西。不是因为它酷，是因为它真的能让 Claude 从"每次都要教"变成"按你的方式干活"。
---

---
url: "https://x.com/vista8/status/2014904809388945554"
requested_url: "https://x.com/i/status/2014904809388945554"
author: "向阳乔木 (@vista8)"
author_name: "向阳乔木"
author_username: "vista8"
author_url: "https://x.com/vista8"
tweet_count: 2
---

## 1
https://x.com/vista8/status/2014904809388945554

朋友问，如何在Claude Code中调用Codex？

订阅ChatGPT送Codex，不用就浪费了。

Codex 虽然慢，但在规划和修Bug场景还是很强的。

快速让AI写了一个Skill，在CC中调用Codex运行，自然语言对话就行，小白友好。

已开源，Github和安装教程见评论区

![](https://pbs.twimg.com/media/G_ZfkuhaEAA_RRG.jpg)

## 2
https://x.com/vista8/status/2014905022358954135

安装方法
1. 跟CC说，安装这个claude skill：https://t.co/WchBJIc56C

2. 终端运行 
npx skills add joeseesun/codex-assistant
---

---
url: "https://x.com/canghe/status/2014998327365140866"
requested_url: "https://x.com/i/status/2014998327365140866"
author: "苍何 (@canghe)"
author_name: "苍何"
author_username: "canghe"
author_url: "https://x.com/canghe"
tweet_count: 1
---

## 1
https://x.com/canghe/status/2014998327365140866

Remotion skills 太强了，在 Claude Code 一句话生成可编辑的动画视频。

这个过程只花了几分钟，太惊艳了。方法也非常简单，一共分为以下几步：

1、下载 remotion skills
npx skills add remotion-dev/skills

选择在 claude code 中使用

2、在 claude code 中直接使用
提示词：调用remotion-best-practices这个 skill 帮我生成新年拜年的动画视频

然后 cc 就会自动帮我用 skills 生成可编辑的动画视频了，甚至可以直接导出视频。

![video](https://pbs.twimg.com/amplify_video_thumb/2014985373080760320/img/NqZEJ4O9LRr2epC_.jpg)
[video](https://video.twimg.com/amplify_video/2014985373080760320/vid/avc1/1668x1080/ljGl1Xax2SeSmAMH.mp4?tag=21)
---

---
url: "https://x.com/treydtw/status/2015030821917466964"
requested_url: "https://x.com/i/status/2015030821917466964"
author: "香蕉Banana (@treydtw)"
author_name: "香蕉Banana"
author_username: "treydtw"
author_url: "https://x.com/treydtw"
tweet_count: 1
---

## 1
https://x.com/treydtw/status/2015030821917466964

分享10个我目前在用的 Skill

1. NotebookLM Skill

神级 Skill，通过它可以直接让 AI 对接 NotebookLM，自动上传资料、做知识问答、生成 PPT、脑图都能搞定。

2. Obsidian Skills

Obsidian CEO 出的 Skill 套件，功能很全：

写出 Obsidian 风格的 Markdown（内链、属性等）
生成 .Base 文件的过滤器和公式
生成 Canvas 无限画布

3. planning-with-files

复刻Manus 的Skil，可以用这个 Skill 来指导其他 Skill 的工作流程。能有效解决上下文飘移的问题。

4. anthropics/skill-creator

自己做 Skill 时候的首选，可以直接通过它创建一个符合最佳实践的 Skill，也可以用它来优化现有的 Skill。

5. frontend-design

前端设计专用，比如可以帮你去掉AI 的渐变色。。

6. Superpowers

Obra 开发的工具包,包含 /brainstorm、/write-plan、/execute-plan 等命令。

可以在你做复杂项目时，讨论方案、和你一起脑暴，还会通过提问来分析问题生成靠谱的方案

7. Rube MCP Connector

通过一个服务器就能把 Claude 连接到大概 500 个应用（Slack、GitHub、Notion 等），不用给每个应用单独配置授权。

8. baoyu-skills

宝玉老师出品的 Skill 套件，比如写长文帮你自动配图的 Skill，自动发推、发公众号的 Skill。

9. 自媒体 Skill 系统

自己开发的 Skill 套装，覆盖日常选题、写脚本、写文案、数据分析等工作。

10. banana-skill-finder
原来用的skill-lookup，感觉不太好使。现在自己重新做了一个，根据skillsmp的api 和 vercel的skillsh来查询。对话过程中如果提出有什么问题会自动寻找合适的skill来帮你解决问题
---

---
url: "https://x.com/lyc_zh/status/2014524364331340021"
requested_url: "https://x.com/i/status/2014524364331340021"
author: "YC (Yucheng Liu) (@lyc_zh)"
author_name: "YC (Yucheng Liu)"
author_username: "lyc_zh"
author_url: "https://x.com/lyc_zh"
tweet_count: 1
---

# 为什么你不应该把所有 Skills 共享给团队

![](https://pbs.twimg.com/media/G_UHM_tXsAADwtd.jpg)

“知识共享”听起来是个不需要讨论的好事。

一个人学会了，全公司受益。一个团队踩过的坑，其他团队不用再踩。这是常识，是效率，是组织智慧的积累。

但我最近开始重新思考这件事。

因为我发现，有些 skill 一旦共享出去，就会腐烂。而有些 skill，如果共享出去，会直接破坏它存在的意义。

## 共享的好处（我们都知道的部分）

先承认共享的价值——这不是一篇”反共享”的文章。

当一个团队花三周摸索出一套高效的 prompt engineering 方法论，把它整理成 skill 共享给其他团队，确实能节省大量时间。我见过一个增长团队开发的「Twitter 爆款分析」skill，共享给内容团队后，整个公司的 Twitter 互动率两周内涨了 40%。这是真实的效率提升。

当运营团队开发了一个自动化社区回复的 skill，让客服团队也用上，确实能提升整体效率。原本需要 3 个人盯着的社区，现在 1 个人配合 AI 就能覆盖，而且回复质量更稳定。

当我写了一个内容创作的 skill，让团队其他成员也能产出相似质量的内容，确实能解放我的时间。以前我是内容瓶颈，所有文章都要过我的手。现在初稿可以并行产出，我只需要把关最后一道。

这些都是真的。共享有价值，很多时候是对的选择。

但不是所有时候。

## 问题一：Context 腐烂（Lossy Compression）

![](https://pbs.twimg.com/media/G_UFxHXWsAE08fE.jpg)

一个 skill 刚被创建时，它是为特定场景、特定团队、特定问题设计的。它”懂”那个 context。

我来讲一个真实的故事。

我们增长团队开发了一个「冷启动社区运营」的 skill。它非常好用——知道什么时候该活跃气氛，什么时候该冷处理，什么样的问题要认真回答，什么样的问题要引导到私聊。这个 skill 是基于我们社区的调性、我们用户的画像、我们产品的特点打磨出来的。

然后产品团队说：我们也想用这个 skill 来运营用户反馈群。

好，共享。

但产品团队的群不太一样。用户画像不同，提问方式不同，期待的回复风格也不同。他们开始提需求：「能不能把这里改得更正式一点？」「能不能加一个处理技术问题的模块？」「我们的用户不喜欢太活泼的语气。」

我改了。Skill 变得更”通用”了。

然后客服团队也想用。他们的场景又不一样——要处理投诉、要安抚情绪、要遵循特定的话术规范。又一轮修改。

三个月后，我回头看这个 skill，已经认不出它了。

它变成了一个「适用于大多数社区场景」的东西。听起来不错？但问题是：它对任何一个具体场景都不够好。增长团队说「感觉没以前好用了」，产品团队说「还是差点意思」，客服团队说「很多地方要手动调」。

一个原本锋利的工具，被打磨成了一个圆润的、无害的、平庸的通用品。

这就是 context 腐烂。

这和组织信息传递中的 lossy compression（有损压缩） 是同一个问题。在金字塔结构里，信息每经过一层就被压缩一次——交易谈判的数小时电话变成 CRM 状态变更，架构辩论的白板争论变成一张 JIRA ticket，走廊里触发产品转向的随口一句变成什么都没有。信息在传递中不断失真。

Skill 的泛化是同样的机制：每次适配一个新场景，就是一次有损压缩。原本针对「我们团队、我们客户、我们产品」设计的精确判断，变成「大多数团队、大多数客户、大多数产品」的模糊指南。

一把为日本料理设计的刀，被要求同时适合切牛排、剁骨头、削水果——最后它什么都能做，但什么都做不好。

泛化的代价是精度。而精度往往才是 skill 有效的关键。

更糟糕的是，一旦开始泛化，就很难回头。因为现在有多个团队依赖这个 skill，任何「退回到更专用版本」的尝试都会引发兼容性问题。你被锁死在「最大公约数」的陷阱里。

## 问题二：数据泄漏

![](https://pbs.twimg.com/media/G_UF1E8W4AAPW7W.jpg)

这是更微妙但更致命的问题。

机器学习领域有个基本原则：训练集、验证集、测试集必须严格分开。如果测试数据泄漏到训练过程中，你的模型看起来表现很好，但那是假的——它只是”记住”了答案，而不是真正学会了。

我在管理团队时发现了完全相同的现象。

例子一：Code Review

我有一套 code review 的 skill。它知道我关注什么——命名规范、边界条件处理、错误信息的可读性、代码的「可删除性」（能不能在未来轻松移除这段代码）。它知道我会在哪些地方挑毛病，什么样的代码能过关什么样的不能。

我从来不把这个 skill 共享给开发者。

为什么？

因为如果我把 code review skill 给他们看，他们就知道了”测试标准”。他们会开始针对这个标准来写代码。

表面上看，代码质量会”提升”——因为提交上来的代码都能通过我的 review 了。但这是假的提升。

他们不是在写更好的代码，他们是在写”能通过 review 的代码”。这两件事听起来像是一回事，但不是。

真正好的代码来自于工程师自己理解什么是好代码，自己形成判断力，自己长出 taste。如果我把评判标准直接告诉他们，我就剥夺了他们形成自己判断力的机会。

例子二：内容审核

我有一个「内容质量评分」的 skill，用来评估团队产出的文章、推文、视频脚本。它会从多个维度打分：信息密度、原创性、可读性、传播潜力。

我不会把这个 skill 给内容团队看。

原因一样：如果他们知道评分标准，他们会开始「针对评分写内容」。

我见过这个现象。有一次我不小心透露了「我很看重开头 50 个字的 hook」，接下来两周，所有人提交的内容开头都变得很精彩——但正文质量下降了。他们把精力都放在了「我知道你会看的地方」，而忽略了其他部分。

例子三：招聘评估

我有一套评估候选人的 skill。它知道我看重什么——不是简历上的光鲜经历，而是思考问题的方式、面对未知的态度、表达的精确程度。

如果我把这个 skill 共享给 HR 或者猎头，会发生什么？

他们会开始筛选「看起来符合这些标准」的候选人。候选人也会开始准备「如何表现得符合这些标准」。

然后我的评估就失效了。我看到的不再是真实的人，而是「针对我的标准优化过的表演」。

这其实就是 Goodhart’s Law（古德哈特定律） 在组织管理中的体现：当一个指标变成目标时，它就不再是一个好的指标。

我的 code review skill 是一个「指标」——它衡量代码质量。 一旦我把它共享给开发者，它就变成了「目标」——他们会针对这个标准优化。 然后这个指标就失效了——它不再能区分真正好的代码和「会通过 review 的代码」。

内容评分、招聘评估，同理。

测试的有效性，依赖于被测试者不知道测试标准。这不是故意刁难，这是测试本身的逻辑。

## 什么时候应该共享：Information Bus vs Local Pods

并不是所有 skill 都有这个问题。关键是区分哪些知识应该放在「共享总线」上，哪些应该保留在「本地 pod」里。

适合放在 Information Bus 上的 skill（可以共享）：

- 纯工具型：怎么用某个 API、怎么配置某个环境、怎么跑某个流程。这些是「事实」，不会因为更多人知道而贬值。你知道怎么调用 OpenAI API，告诉别人，他也会了，你的知识没有任何损失。
- 知识沉淀型：踩过的坑、最佳实践、操作手册。「我们试过 X 方案，失败了，原因是 Y」——这种知识共享出去只有好处。没有人会因为知道这个而「优化」出什么问题。
- 效率提升型：自动化脚本、模板、prompt 库。「这个 prompt 可以让 Claude 写出更好的技术文档」——共享它，大家都写出更好的文档，皆大欢喜。

这些 skill 共享出去，价值就是增加的。它们是「事实性知识」，没有”泄漏”风险，也不太容易因为泛化而腐烂（因为它们本来就不太依赖特定 context）。

应该保留在 Local Pod 里的 skill（不该共享）：

- 评判型：code review、内容审核、质量把关、绩效评估。这些 skill 的价值在于「被评判者不知道评判标准」。一旦标准公开，评判就变成了「合规检查」——你只能检查是否符合已知标准，而无法发现真正的问题。
- 决策型：优先级判断、资源分配、方向选择。这些 skill 高度依赖 context——当前的市场环境、团队状态、竞争格局。把它们泛化成「通用决策框架」，往往会丢失最关键的判断依据。
- 培养型：任何你希望对方「自己学会」而不是「照着做」的东西。好的导师不会把所有答案直接告诉你，而是创造让你自己发现答案的环境。把「如何做判断」直接告诉别人，就剥夺了他们「学会判断」的机会。

这些 skill 一旦共享，要么会腐烂（因为评判标准是 context-dependent 的），要么会造成”数据泄漏”（因为知道标准会改变行为）。

这和组织架构里「什么信息应该全局共享，什么信息应该局部保留」是同一个问题。一个健康的组织不是「所有人知道所有事」，而是「对的人知道对的事」。信息的价值有时候恰恰在于它的「局部性」——只有特定的人在特定的时候知道。

## 一个反直觉的结论

![](https://pbs.twimg.com/media/G_UFuyzWAAAA4KE.jpg)

效率的最大化，有时候需要信息的不对称。

这听起来很政治不正确。我们不是应该追求透明、开放、知识共享吗？硅谷文化不是鼓励「radical transparency」吗？

但仔细想想：

- 考试为什么不提前公布答案？ 因为考试的目的是测试你是否「学会了」，而不是测试你是否「能找到答案」。公布答案会让考试失去意义。
- 为什么盲测比公开测试更可信？ 因为当被测试者知道自己在被测试时，行为会改变。药物临床试验要双盲，用户研究要做 A/B 测试而不是直接问用户，都是这个道理。
- 为什么好的教练不会把所有技巧一次性告诉你？ 因为技巧是要「长」在身体里的，不是「记」在脑子里的。告诉你「挥拍时手腕要这样转」没用，你需要自己挥一千次拍，然后在某一次突然「悟」到。
- 为什么师傅带徒弟要「留一手」？ 传统观点认为这是自私，但另一个解释是：有些东西说出来就「不灵」了。徒弟需要自己去悟，师傅能做的是创造悟的条件，而不是直接给答案。

有些知识，你知道得太早，反而会阻碍你真正学会它。

有些标准，你知道得太清楚，反而会让你学会”应付标准”而不是”达到标准”。

有些 skill，它的价值恰恰在于不被共享。

透明是好的，但透明不等于「所有信息对所有人开放」。透明是指「规则公开」，不是指「答案公开」。

## 我的做法

![](https://pbs.twimg.com/media/G_UF4WkXkAETiwo.jpg)

现在我会把 skill 分成两类：

公开 skill（放在共享库）

- 所有工具使用指南
- 技术栈配置和部署流程
- 踩坑记录和解决方案
- 通用 prompt 模板
- 自动化脚本

这些 skill 任何人都可以用，鼓励大家贡献和改进。它们是组织的「公共基础设施」。

私有 skill（仅特定角色可见）

- 我的 code review skill：只有我用。开发者提交代码，我用这个 skill 辅助 review，但他们不知道我具体看什么。这保证了 review 的有效性。
- 内容质量评判 skill：只有我和主编用。内容团队知道「会有质量评估」，但不知道具体评估维度。这让他们专注于「写好内容」而不是「通过评估」。
- 招聘评估 skill：只有面试官用。HR 和猎头知道我们在找什么类型的人（这是公开的），但不知道面试中具体评估什么（这是私有的）。
- 优先级决策 skill：只有管理层用。团队知道「有一套优先级框架」，但具体权重和判断逻辑不公开。这避免了「所有需求都被包装成高优先级」的博弈。

这些 skill 的价值，恰恰在于被评估的人不知道评估标准，被决策影响的人不知道决策算法。

这不是在搞信息不对称的权力游戏。这是在保护一个系统的有效性。

## 写在最后

“知识就是力量”这句话有个前提：是你自己获得的知识。

被直接”喂”进来的知识，和自己摸索出来的知识，价值是不一样的。前者是信息，后者是能力。

一个开发者读了我的 code review skill，他获得了「信息」——他知道我会看什么。但他没有获得「能力」——他不知道为什么这些东西重要，不知道在新的场景下该怎么判断。

真正的能力是「可迁移的」。它不是一套规则，而是一种直觉，一种 taste，一种「看一眼就知道对不对」的感觉。这种东西没法通过共享 skill 来传递，只能通过自己去试、去错、去悟来获得。

有些 skill，最好的共享方式，是让对方自己也长出一套——而不是直接把你的给他。

下次你想把一个 skill 共享给团队的时候，先问自己两个问题：

1. 这个 skill 共享出去，会不会因为泛化而腐烂？

如果它高度依赖特定 context，共享可能会毁掉它。

2. 这个 skill 共享出去，会不会造成「数据泄漏」？

如果它是一个评判标准，公开它可能会让被评判者学会「应付」而不是「达标」。

如果两个问题的答案都是「会」，也许保留它，才是真正对团队好的选择。

知识共享是好事。

但不是所有知识都应该共享。

最稀缺的知识，往往是那些一旦共享就会失效的知识。
---

---
url: "https://x.com/Context7AI/status/2014702620758118768"
requested_url: "https://x.com/i/status/2014702620758118768"
author: "Context7 (@Context7AI)"
author_name: "Context7"
author_username: "Context7AI"
author_url: "https://x.com/Context7AI"
tweet_count: 1
---

## 1
https://x.com/Context7AI/status/2014702620758118768

Introducing Context7 Skills! 🎉

◆ We extracted 24k skills from 65k repos
◆ Skills for Tailwind, React, Better-Auth, etc.
◆ Install in a single CLI command

Perfect for Cursor, Claude Code &amp; others 👇 https://t.co/mHItwWBMu1

![video](https://pbs.twimg.com/amplify_video_thumb/2014701746841350144/img/FyLSaEhIENn2nADb.jpg)
[video](https://video.twimg.com/amplify_video/2014701746841350144/vid/avc1/1840x1080/iI9TMTEi2-FKkuaP.mp4?tag=21)
---

---
url: "https://x.com/idoubicc/status/2014630939104776411"
requested_url: "https://x.com/i/status/2014630939104776411"
author: "idoubi (@idoubicc)"
author_name: "idoubi"
author_username: "idoubicc"
author_url: "https://x.com/idoubicc"
tweet_count: 2
---

## 1
https://x.com/idoubicc/status/2014630939104776411

我的桌面 Agent 产品 WorkAny 开源了。

主要特性：

1. 以 Claude Code 为 Agent 运行时，可以完成各类任务
2. 以 Codex 为运行沙盒，可以在隔离环境执行脚本
3. 支持整理文件、生成网站、生成 PPT / Excel / Word 等日常办公任务
4. 支持 MCP / Agent Skills，可玩性高
5. 支持自定义模型，可以接入 OpenRouter、火山引擎、Kimi、智谱等供应商
6. 支持复用本地的 Claude Code 订阅套餐，无需额外付费
7. 支持并行任务，异步查看结果
8. 支持多套主题，样式美观

代码已发布到 Github，目前为开发版，需要自行编译可执行文件，依赖本地的 node 环境。

欢迎试用，感谢支持。

![](https://pbs.twimg.com/media/G_VnLGmbAAI0Ap7.jpg)
![](https://pbs.twimg.com/media/G_VnNc3aQAAwDw6.jpg)
![](https://pbs.twimg.com/media/G_VnQQ6bwAAx83m.jpg)
![](https://pbs.twimg.com/media/G_VnVAVWQAAJGDs.jpg)

## 2
https://x.com/idoubicc/status/2014631547857719454

项目地址：https://t.co/OQyKdAu6W6 https://t.co/9yMvq72KKp

![](https://pbs.twimg.com/media/G_VotcXWEAEsZw-.jpg)
---

---
url: "https://x.com/YukerX/status/2014537059504161173"
requested_url: "https://x.com/i/status/2014537059504161173"
author: "Yuker (@YukerX)"
author_name: "Yuker"
author_username: "YukerX"
author_url: "https://x.com/YukerX"
tweet_count: 1
---

# Claude Code 零基础进阶：高手都在用的 Skill 2.0 架构指南（附完整步骤）

![](https://pbs.twimg.com/media/G_USScEaAAAFd9_.jpg)

如果你之前阅读过我的文章《小白也能解锁 Claude Code 的秘密武器：Skills》的话，那么在 Skills 越来越火热的当下，你或许会抱有以下的疑问：

> Skills 不是应该只有一个 Markdown 文件吗？为什么我看别人 Remotion 的 Skills 都有一大堆 Rules 什么之类的！
> 为什么我 SKILL.md 写的那么长，反而感觉它越来越笨了呢？
> 我该怎么样做出别人那种特别厉害的 Skill 呀？

假若你曾冒出来过这样的念头，那今天这篇文章，将会彻底解决你的疑问和顾虑。我们将跳出 SKILL.md 的单文件思维，进入“文档架构”的世界。

这期文章篇幅会较长，但无需担心，依旧是小白也能看懂的内容，并且配合马上能上手练习的实战案例，相信你看完后，也能完成属于你的 Skill 作品！

> 今天我们要讲的是 -- Skills 文档架构。

# 第一章：为什么你的 SKILL.md 不够用？单文件思维的两大“困境”

在学习任何新技能的初期，我们总是倾向于最简单直接的方法。对于 Claude Code Skills 而言，这意味着把所有东西都塞进 SKILL.md。这在入门阶段完全没问题，但当你试图构建一个真正强大的、可长期使用的 Skill 时，这种单文件思维模式的弊端就会暴露无遗。

## 困境一：上下文的“无形枷锁”

这个大家都应该知道，当你将所有指令、规则、示例代码、参考文档全部堆砌在一个 SKILL.md 中时，每一次 Skill 的触发都变成了一次沉重的“记忆负担”。Claude 就像一个需要时刻背着一本厚重百科全书的学者，即使只是为了查找一句话，也必须扛着整本书。

这将会导致：

- 性能下降：加载和处理庞大的 SKILL.md 会消耗更多时间，让交互变得迟钝。
- 关键信息丢失：当上下文接近极限时，模型可能会“遗忘”掉文件开头或中间的关键指令，导致执行效果大打折扣，出现所谓的“指令漂移”。
- 预算超支：在某些计费模式下，更大的上下文意味着更高的成本。

## 困境二：维护的“噩梦迷宫”

一个超过 500 行的 SKILL.md 就是一个维护的噩梦。想象一下，你现在需要更新其中关于“数据库连接池”的最佳实践。你不得不在这个巨大的文本文件中，通过 Ctrl+F 小心翼翼地定位，然后像拆弹专家一样修改内容，同时祈祷不会影响到其他不相关的部分。

这种高耦合的结构，会带来诸多的问题：

- 逻辑混乱：做到后面，你自己都看不懂自己在做什么
- 可读性差：就算你能看懂，你的同事想要用，也得掉层皮
- 修改风险高：原本能跑的，你改完可能就跑不了了

# 第二章：Skill 2.0的核心 - 像搭乐高一样构建你的“技能”

告别了单文件的混乱，我们迎来的是 Skill 2.0 的核心思想：模块化与渐进式披露（Progressive Disclosure）。这个听起来有点“学术”的词，其实原理非常简单，就像我们日常阅读一本书：

- 先看目录（SKILL.md）：我们首先浏览目录，对全书的结构有一个宏观的了解。
- 按需阅读章节（引用文件）：当我们对某个特定章节感兴趣时，才会翻到那一页去深入阅读。

Claude Code 使用 Skill 的方式与此完全相同。它不会一口气吞下所有信息，而是先加载一个轻量的“目录” —— SKILL.md，然后根据任务的需要，通过文件链接去“翻阅”更具体的“章节”——也就是我们拆分出去的各种 .md，.py 或 .json 文件 。

这种架构的精髓在于，将一个庞大的知识体系，拆解成一个个独立、内聚、可管理的“知识积木”。然后，通过 SKILL.md 这个“蓝图”，将这些积木有机地组织起来。这不仅解决了上下文的“无形枷锁”，更让维护、协作和扩展变得前所未有的简单。

> 👹文档架构的“规则怪谈”如下：

基于这一核心思想，社区和官方的最佳实践中沉淀出了两种最经典、最实用的文档架构模式：知识库型（Knowledge Base） 和 工作流型（Workflow）。

## 模式一：知识库型架构 （Knowledge Base）

适用场景：当你的 Skill 主要是为了给 Claude 提供一套静态的、结构化的知识时，这种模式是你的不二之选。比如：

- 公司内部的 API 文档
- 特定编程框架（如 React, Vue）的最佳实践
- 团队共享的设计规范或写作风格指南

核心理念：将知识“原子化”。每一个独立的知识点都应该是一个独立的文件，而 SKILL.md 则扮演着这些知识点的“索引”或“目录”的角色。

目录结构：

SKILL.md 怎么写：

工作原理：

当用户问 "公司的 OKR 是什么意思" 时，Claude 会：

1. 先看 SKILL.md，发现这是个术语问题
2. 打开 knowledge/术语表.md，找到 OKR 的解释
3. 回答用户

> Claude Code 不会去打开 "产品FAQ" 或 "报销流程"，因为跟当前问题无关。这就是"按需取用"的威力。

⚠️也就是说， 如果 SKILL.md 里面没有提及到需要使用某些文件，某些文件将永远不会被用上！

![](https://pbs.twimg.com/media/G_SInYhbAAoMOSu.png)

## 模式二：工作流模式 -- 打造你的“自动化流水线”

适合场景：当你的 Skill 是要完成一个多步骤的任务时。

典型例子：

- 写周报（收集信息 → 整理 → 按格式输出）
- 做会议纪要（听录音 → 提取要点 → 生成文档）
- 发布文章（检查格式 → 配图 → 发布到平台）

核心理念：将任务“流程化”。把一个复杂的任务拆解成一系列线性的、可独立执行和验证的步骤，每个步骤都是一个独立的文件。

推荐目录结构：

![](https://pbs.twimg.com/media/G_SFYuXX0AA5dXE.jpg)

SKILL.md 怎么写：

工作原理：

> 当用户说"帮我写周报"时，Claude 会：

1. 看 SKILL.md，了解整体流程
2. 依次执行 step1 → step2 → step3
3. 在 step3 时，打开"周报模板"来格式化输出
4. 每完成一步，在清单上打勾 ✓

这就像一条流水线，每个步骤都清清楚楚，不会漏也不会乱！

## 知识库 vs. 工作流：我该如何选择？

当然，在现实世界的复杂项目中，这两种模式并非完全互斥。你完全可以在一个工作流型的 Skill 中，引入一个 reference/ 目录来存放知识库型的参考文档。

掌握了这两种核心架构，你就拥有了构建任何复杂 Skill 的基础。接下来，我们将进入实战环节，手把手带你从零开始，构建一个既实用又结构精良的 Skill！

# 第三章：实战演练！10 分钟打造你的第一个“架构化” Skill

理论讲完了，现在我们来实战！我会带你从零开始，用 10 分钟打造一个真正好用的"AI 周报助手"。

这个案例之所以选周报，是因为：

1. 人人都要写周报：不管你是程序员、产品经理还是运营，都能用
2. 效果立竿见影：做完马上就能用，周五下班前再也不用愁了
3. 完美展示架构思想：既有工作流，又有知识库！

💡下面较长篇幅都是模板文件，以供大家 Copy & Paste 体验！大家实操完的结构应该如下：

![](https://pbs.twimg.com/media/G_T7CFPXYAAWwjd.jpg)

🔥前几步大家只需要跟着 Copy & Paste 即可，一切感悟都会在“最后一步”为大家打通！

## 第一步：创建文件夹结构

打开你的终端（或者文件管理器），创建以下结构：

创建完成后，你应该有这样的目录：

## 第二步：编写“写作规范” （Rules）

这是给 Claude 的"写作指南"，告诉它周报应该怎么写：

## 第三步：编写"周报模板" ( report-template.md )

> 这是周报的输出格式，Claude 会严格按照这个模板来生成内容：

## 第四步：编写工作流步骤

1️⃣ Workflow 第一步：搜集信息 （step1-collect.md）

2️⃣ Workflow 第二步：整理内容 （step2-organize.md）

3️⃣ Workflow 第三步：生成周报 （step3-generate.md）

![](https://pbs.twimg.com/media/G_T6uzAacAAfxLe.jpg)

## 第五步：编写主控文件 (SKILL.md) ！

这是整个 Skill 的"大脑"，把所有东西串起来：

## 第六步：见证奇迹！

现在，在确保了 Skills 已经存放在~/.claude/skills/ 目录下后，可以尝试在 Claude Code 中输入：

如果你能在 Claude Code 里面，看到以下画面，那就代表着 Skill 已经存在于你的目录了：

当你输入指令，并且把这一周的工作告诉 Claude Code 后，你能惊讶的发现，它居然真的在按照你的 Workflow 设定工作！正如下图一样：

Claude Code 会：

1. 先问你本周做了什么
2. 帮你整理、分类、提炼
3. 按照模板生成一份漂亮的周报

从此，周五下班前的周报焦虑，不复存在！ 🎉

# 第四章：三个让 Skill 更强大的进阶技巧

Skill 能做到的设置， 远远不止周报生成器这么简单，它甚至能够内嵌 Program 来应付各种需求，但限于篇幅有限，今天我们还是以周报生成器作为例子，以便大家理解！

## 技巧一：用配置文件实现"一键切换"

如果你需要在不同场景下使用同一个 Skill（比如给不同部门写周报，格式要求不同），可以用配置文件来实现。

里面的 Json 格式文件，可以设置好结构化数据，如下：

最后，必须要在 Skill.md 里面引用文件，否则不会生效！

这样，切换部门只需要改一下配置文件的引用，不用改任何指令。

## 技巧二：用“禁止清单”防止 Claude Code犯错

> 有时候，告诉 Claude "不要做什么" 比告诉它 "要做什么" 更有效

我们可以在 Rule/ 目录下创建一个 dont-do.md ：

然后同样的，必须在 SKILL.md 中强调：

## 技巧三：用“检查清单”确保质量

在最后一步加一个自检环节，让 Claude 在输出前自己检查一遍。

可以在 Workflow 中，多加一个自检的步骤：

这就像给 Claude 配了一个"质检员"，大大减少低级错误。

# 结语：你不是在写 Skill，你是在构建一个“数字员工”

从最初那个臃肿、混乱的 SKILL.md，到现在我们面前这个结构清晰、权责分明的“企业级黄金架构”，我们走过了一段从“炼金术”到“现代化学”的旅程。我们不再满足于偶然调配出有效的“魔法药水”（Prompt），而是开始系统性地构建稳定、可预测、可扩展的“分子结构”（Skill 架构）。

这，就是 Claude Code Skills 2.0 的精髓所在。

当你开始用“架构”的眼光去审视你的 Skill，你赋予 Claude 的，就不再是一条条孤立的指令，而是一个完整的、结构化的“数字大脑”。

记住，你所做的，远不止是提升 AI 的工作效率。你是在定义一种全新的、与人工智能深度协作的未来。在这个未来里，我们不再是 AI 的“使用者”，而是它的“设计者”和“架构师”。我们构建的每一个结构精良的 Skill，都是在为这个智能时代，添上一块坚实的基石。
---

---
url: "https://x.com/GitHub_Daily/status/2014548706117448091"
requested_url: "https://x.com/i/status/2014548706117448091"
author: "GitHubDaily (@GitHub_Daily)"
author_name: "GitHubDaily"
author_username: "GitHub_Daily"
author_url: "https://x.com/GitHub_Daily"
tweet_count: 1
---

## 1
https://x.com/GitHub_Daily/status/2014548706117448091

用 Claude Code 开发项目，配置文件散落各处，每次都要翻文档找命令、写 Hook、调 Agent，工作效率颇为低下。

偶然看到 Everything Claude Code 这个开源项目，作者是 Anthropic 黑客松获奖者，把 10 个月实战积累的配置全部开源了。

包含生产级的 Agent、Skill、Hook、Command、Rule 和 MCP 配置，涵盖测试驱动开发、代码审查、安全检测、性能优化等完整工作流。

GitHub：https://t.co/G0Vt1Cwgsd

提供一键安装的插件模式，也支持手动复制单个组件。内置 9 个专业 Agent，包括规划、架构、测试、审查等，以及 20 多个可复用 Skill，还有自动触发的 Hook 机制。

更重要的是，项目配套两份详细指南：基础指南讲解配置结构和上下文管理；进阶指南深入讲解令牌优化、会话记忆持久化、验证循环、并行化策略等高级技巧。

如果你正在用 Claude Code 开发项目，或者想系统性地提升 AI 辅助编程效率，这个项目值得收藏学习。

![](https://pbs.twimg.com/media/G_UdW4gWgAAidap.jpg)
![](https://pbs.twimg.com/media/G_UdW4AbAAA8ql7.jpg)
---

---
url: "https://x.com/verysmallwoods/status/2014830889138626883"
requested_url: "https://x.com/i/status/2014830889138626883"
author: "VerySmallWoods (@verysmallwoods)"
author_name: "VerySmallWoods"
author_username: "verysmallwoods"
author_url: "https://x.com/verysmallwoods"
tweet_count: 1
---

## 1
https://x.com/verysmallwoods/status/2014830889138626883

又一个 😶‍🌫️

Stitch Agent Skills 正式登场。

通过 add-skill 命令，就能 Stitch 的设计能力直接注入自己的项目。
🎨 design-md：从 Stitch 项目自动生成 https://t.co/xhUTu4ieBL 设计规范，彻底告别 UI 不一致。
⚛️ react-components：将 Stitch 设计一键转为生产级 React 组件。

Web 应用开发是近期 Agent Skills 的主战场 🥸

> Author: Stitch by Google (@stitchbygoogle)
> URL: https://x.com/stitchbygoogle/status/2014478393170133139
>
> Developer Week Day 4. ⚡️
>
> Introducing Stitch Agent Skills.
>
> Powered by the add-skill installer, you can now inject Stitch expertise directly into your project with a single command.
>
> 🎨 design-md: Generates a "source of truth" design[dot]md file for your design rules from your Stitch project. No more inconsistent UI.
>
> ⚛️ react-components: Turns Stitch designs into production-ready React components with design token consistency.
>
> Submit your own skills or request new ones in the repo. Let’s build the future of vibe design together. 👇
---

---
url: "https://x.com/dotey/status/2014014507291467874"
requested_url: "https://x.com/i/status/2014014507291467874"
author: "宝玉 (@dotey)"
author_name: "宝玉"
author_username: "dotey"
author_url: "https://x.com/dotey"
tweet_count: 2
---

## 1
https://x.com/dotey/status/2014014507291467874

我自己也受不了从 Agent 里面调用 Gemini Web 画图了，太不稳定了。新增加了 baoyu-image-gen Skill，基于官方 API ，支持 GOOGLE_BASE_URL，需要配置 GOOGLE_API_KEY

npx skills add jimliu/baoyu-skills https://t.co/Z6ruDwAmG5

![](https://pbs.twimg.com/media/G_M27n7XYAUo_ZR.jpg)
![](https://pbs.twimg.com/media/G_M3YL0XYAg0v7C.jpg)

## 2
https://x.com/dotey/status/2014014707955380258

相关代码：https://t.co/1cJAqfv1sB
---

---
url: "https://x.com/brad_zhang2024/status/2014362069781639203"
requested_url: "https://x.com/i/status/2014362069781639203"
author: "烟花老师 (@brad_zhang2024)"
author_name: "烟花老师"
author_username: "brad_zhang2024"
author_url: "https://x.com/brad_zhang2024"
tweet_count: 1
---

## 1
https://x.com/brad_zhang2024/status/2014362069781639203

这个专门用来吹🐂🍺的 skill 太好用了！hhhh

chuinb-skill 

一句话就能帮你搜索，分析，下载图片，视频片段，
模拟对应的场景对话，让你在任何场合可以游刃有余的吹🐂🍺

已经开源：
https://t.co/PiPRQNnnsB

想象一下这些场景：
下周要和投资人聊区块链，但你完全不懂？
想转行到新能源行业，需要快速了解行业全貌？
朋友约你聊咖啡文化，你想显得很懂行？

chuinb-skill会帮你：
1 用最简单的语言解释行业本质（连12岁小孩都能听懂）
2 教你行业黑话，让你说话像个内行人
3 介绍必知的关键人物和经典案例
4 生成精美的图片和视频，让学习更生动
5 提供闪卡和测验，帮你巩固记忆
6 最后保存成一份可以随时翻阅的笔记

现在，开始你的表演，showtime!!

图片内容是我测试的两个例子：
“如何成为专业的影评人” 和 “威士忌行业速成指南”

![](https://pbs.twimg.com/media/G_RxwgaWMAA_rSH.jpg)
![](https://pbs.twimg.com/media/G_Rx8VrbsAEu0km.jpg)
![](https://pbs.twimg.com/media/G_RyK8XawAAJ52X.jpg)
---

---
url: "https://x.com/brad_zhang2024/status/2014334520636657751"
requested_url: "https://x.com/i/status/2014334520636657751"
author: "烟花老师 (@brad_zhang2024)"
author_name: "烟花老师"
author_username: "brad_zhang2024"
author_url: "https://x.com/brad_zhang2024"
tweet_count: 1
---

## 1
https://x.com/brad_zhang2024/status/2014334520636657751

根据乔木老师这篇帖子做了 zimage-skill 可以生成每天 2000 张免费图片，按照readme 文档说明安装即可

基础用法：
1：生成一张可爱的柴犬图片
2：画一个宇航员在月球上
3：创建一张抽象艺术画

进阶用法：
1：生成一张图片：一只橘色的猫咪坐在窗台上，窗外是下雨的城市夜景，温暖的室内灯光，电影感的构图，4K高清

2：画一幅画：中国水墨画风格的山水，远处有云雾缭绕的山峰，近处有一叶扁舟，意境悠远

安装方式：在 CC 中说：
帮我安装 zimage-skill，仓库地址是 https://t.co/r57St9uAAk

> Author: 向阳乔木 (@vista8)
> URL: https://x.com/vista8/status/2011404171279315330
>
> 无论写公众号，还是 X 长文，都需要配图。
>
> 从经验看，Nano Banana Pro 和 即梦4.5生图都很好。
>
> 用API多少都要花钱，反向代理难度又高。
>
> 搜免费配图API，发现阿里巴巴的Z-Image每天可免费生2000张图！
>
> 量大又免费，阿里现在也是菩萨啊！
>
> 解读过 z-image 论文，很巧妙，中文支持也不错。
>
> 简明教程如下：
>
> ① 注册阿里魔搭，到下图页面，点红框，复制API代码。
>
> （默认会有API，很贴心）
>
> ② 跟Claude Code或OpenCode对话说：
>
> 基于下面代码创建一个Claude Skill：【粘贴代码】
>
> 当然，直接当API用也行。
>
> 做成Skill，方便跟其他写文章Skill组合。
>
> ---
>
> 页面地址不好找，我放评论区，如果觉得有用，请一键三连，哈哈哈哈~~
---

---
url: "https://x.com/chengfeng240928/status/2014101207816741127"
requested_url: "https://x.com/i/status/2014101207816741127"
author: "成峰 (@chengfeng240928)"
author_name: "成峰"
author_username: "chengfeng240928"
author_url: "https://x.com/chengfeng240928"
tweet_count: 1
---

# Claude Skills 自更新：这个设置让AI 越用越聪明！

![](https://pbs.twimg.com/media/G_OFAaGaIAAgTDB.jpg)

现在，我所有的内容——文章、视频——

都是通过我的写作 Skills 来写的。



以前，写作内容非常不稳定。

有时候写得好，有时候写得差。

全靠状态。



现在不一样了。

写作非常快，内容很稳定，数据也不错。



![](https://pbs.twimg.com/media/G_OFOIbaIAQ9tuI.jpg)



区别在哪？

我把写作习惯绑进了 Skills。



以前，80%的认知资源花在执行上：格式、排版、用词。

没空间思考原理。



现在不一样了。

我把执行交给 Skills。



格式、排版、流程——它记住了，自动跑。

我的认知资源释放出来，花在原理研究上。



这就是为什么现在写得又快又稳。

不是我变厉害了，是我把精力花对地方了。

很多人纠结：AI写的有AI味怎么办？



我不这么想。



我的价值是让大家理解内容。

能理解、有收获，就是好内容。



思想才是最重要的！

谁写的，不重要。

![](https://pbs.twimg.com/media/G_OFQtlWMAEDn4v.jpg)



一个一个说。

## 1.原理研究（最重要）

Skills 不是让 AI 帮你干活。

是让 AI 按照你研究出来的原理干活。



原理从哪来？

从高手那里学，从实践中总结。

举个例子：



我从影视飓风的 Tim 那里学到一个原理：

文章的短视频化。



具体来说，就是"关键词原理"：

- 去掉无谓内容
- 凸显重点关键词
- 形成小短句
- 不要长段落



这就是原理研究。

研究清楚之后，写进 Skills。

以后每次写作，自动按这个原理来。



关键：原理决定上限，执行决定下限。

## 2.热加载（基础条件）

Skills 有一个特性：热加载。



你改了 SKILL.md，下次对话自动生效。

不用重启，不用配置。



这意味着什么？

你可以边用边改。

发现问题，立刻修正。

## 3.过程反馈

用的时候，随时给反馈。



> "这里不对，应该这样..."
> "这个风格我喜欢，以后都这样"
> "这段删掉，太啰嗦了"



AI 会把你的反馈记下来。

下次自动避免/继续。



你说一次，它记一辈子。

## 4.数据反馈

发布之后，看数据。



数据好 → 强化这个方向

- 数据差 → 分析原因，调整



举个例子：

- 某篇文章数据特别好
- 分析：开头用了"身证"，读者信任感强
- 写进 Skills：以后开头优先用身证



成功可以复制，失败可以避免。

## 5.自更新机制（怎么操作）

具体怎么做？

让 AI 帮你写一个自更新 Skill。



你只需要跟 AI 说：



> 帮我写一个自更新 skill。
> 
> 要求：
> 1. 先搜索 .claude/skills/ 里现有的 SKILL.md，学习格式
> 2. 这个 skill 的作用是：当我用完某个 skill 后，
>    能收集我的反馈，自动更新到那个 skill 里
> 3. 触发方式：/自更新
> 4. 执行逻辑：
>    - 搜索我最近使用的 skill
>    - 对比这次的使用过程，看哪里可以优化
>    - 找到对应位置，更新进去



AI 会按照 Skills 的标准格式，帮你生成一个自更新 skill。

保存到 .claude/skills/自更新/SKILL.md 就能用了。



以后每次用完写作 skill，输入 /自更新。

说："开头太长了，控制在3句以内"

AI 自动帮你改到主 skill 里。



你说一次，它记一辈子。

## 通用规则 → 你的定制方案

![](https://pbs.twimg.com/media/G_OFFhyaIAEx5yb.jpg)



Skills 从通用规则，变成只属于你的定制方案。

Skills 会拉大人和人之间的差距。



![](https://pbs.twimg.com/media/G_OFClYaIAIc9o5.jpg)



未来不是人和AI的对比，

是人+AI 和 人+AI 的对比。



差距在哪？

在于你的AI有没有记住你是谁。



同样用 Claude，

有人每次从零开始，

有人的 AI 已经记住了他所有习惯。



从0到1，学习skills

推荐一下黄叔的课程，skills教程非常全👍

![](https://pbs.twimg.com/media/G_OFIIyaIAEbi11.jpg)



![](https://pbs.twimg.com/media/G_OFLJjWIAAnZTu.jpg)
---

---
url: "https://x.com/gregpr07/status/2014258487828807950"
requested_url: "https://x.com/i/status/2014258487828807950"
author: "Gregor Zunic (@gregpr07)"
author_name: "Gregor Zunic"
author_username: "gregpr07"
author_url: "https://x.com/gregpr07"
tweet_count: 2
---

## 1
https://x.com/gregpr07/status/2014258487828807950

Introducing: Browser Use CLI + Skill (100% OSS)👀

Give your Claude Code/Codex agent a browser. Perfect for local dev🧙

"go to localhost:3000, tell me what's wrong with the UI and keep improving it until it looks pretty". It just works.

 Works with:
 ✅ Headless (fast)
 ✅ Your real Chrome (with logins)
 ✅ Cloud browsers (proxies + anti-detection)

 2-line skill install. Link below ↓

![](https://pbs.twimg.com/media/G_QUnHmacAAPZXQ.jpg)

## 2
https://x.com/gregpr07/status/2014258489561174515

https://t.co/mCOH1tFi2X
---

---
url: "https://x.com/Khazix0918/status/2013812311388229792"
requested_url: "https://x.com/i/status/2013812311388229792"
author: "数字生命卡兹克 (@Khazix0918)"
author_name: "数字生命卡兹克"
author_username: "Khazix0918"
author_url: "https://x.com/Khazix0918"
tweet_count: 1
---

# Skills的最正确用法，是将整个Github压缩成你自己的超级技能库。

![](https://pbs.twimg.com/media/G_J_fZpbgAA_zsp.jpg)

我一直觉得，重复造轮子是一件特别呆逼的事情，互联网三十年，开源世界大神这么多，其实你能想象到的绝大多数需求，都有大佬和真神们，在前方铺路，做出了现成的产品，然后开源了出来，给非常非常多的人用。

其实现在非常多的一些商业APP，特别是一些所谓的格式工厂、压缩之类的，绝大多数都是把一些大佬的开源工具，做个前端，给大家用。

之前我觉得没啥问题，确实，Github上面很多的开源项目，都是没有GUI的，全部需要部署，部署以后还是用命令行操作，真的，光环境这一条，就能卡死绝大多数的普通用户。

我自己，之前就是被挡在门外的普通用户。

有太多太多好玩的、实用的、很屌的开源项目，我用不了了。

比如格式转化这破事，没有AI之前，我每次就是去Google搜，MP3转WAV...

![](https://pbs.twimg.com/media/G_J9dRuaoAMTXAN.jpg)

然后就看着各种各样你也不知道是不是有刺客的链接，在向你招手。。。

所以，Skills一来，从文件结构上，它是可以把脚本和Prompt打包在一起的，这一点，跟单Prompt或者脚本完全不一样，再加上现在一些Coding能力强的基模和Agent，我觉得，它天然的擅长把很多的大佬们的开源项目Skill化，从而在Agent里面，为我所用。

而且你要相信那些历史悠久的经典开源项目，经历了无数的时间和使用者的鞭打，不管是成功率还是稳定性还是效率，都远超绝大多数的你根据需求，让AI临时去写的一些代码...

所以就搞了这么个东西，当你在OpenCode或者Claude Code这种支持Skills的产品里，只要你装了那个Claude官方那个能生成Skills的Skill，也就是skill-creator，打包Github上的开源项目，也是完全没问题的。

![](https://pbs.twimg.com/media/G_J83y1agAAsT_x.jpg)

这种方式，就能最快速度，越过所谓的本地整合包，变成一个类似于Agent的产物，让你能快速的用上。

比如，我把视频处理的开源项目FFmpeg和图片视频处理项目ImageMagick，封装成了一个多模态素材处理的Skill，它大概就是这个效果。

![](https://pbs.twimg.com/media/G_J99E5WEAALLgF.png)

我在我的文章中发现一个有趣的评论，引起了我的注意。

![](https://pbs.twimg.com/media/G_J-cFmbMAAqqIQ.jpg)

这个评论的问题没啥毛病，因为github上那么多开源项目，离大众肯定还是非常的遥远，我因为知道有特定的项目可以去处理特定的事，所以封装成Skill就特别的简单，但是大多数的普通人，可能连github是什么都不知道，那怎么封装呢？

这确实是个问题。

我当时想了两分钟，然后我一寻思，不对啊，这不都有AI了吗...

于是，我就回了一句，然后没想到，

引起了好几个朋友非常正向的反馈。

![](https://pbs.twimg.com/media/G_J8qXqaoAQ2xhu.jpg)

这个时候，我才意识到，其实，我的很多的小技巧，对于蛮多人来说，还是挺有价值的。

所以这块，我觉得可以单独拎一篇文章，来给大家讲一讲，普通人怎么把整个github，当成自己的弹药库，做成skill，让自己真正的，变得三头六臂无所不能。

比如，我自己现在，就已经封装了很多的skills。

![](https://pbs.twimg.com/media/G_J9p86WwAAaqrZ.jpg)

这个管理skills的skill，也是我自己建的一个skill，要不然感觉每次进到文件里看太麻烦了，我就可以直接用这个skill，对我本地的所有skill进行卸载删除修改优化操作...

举一个例子。

我相信大家经常都有一个需求，就是去各种视频网站上，下载视频，比如Youtube、B站等等。

我自己也有。

那我们就可以直接打开ChatGPT，选中GPT-5.2 Thinking（目前我认为搜索能力最好、幻觉程度最低的模型），当然，你用别的也行，一般来说问题都不大。

然后直接提出你的问题：

有没有那种就是去各种视频网站上，下载视频，比如Youtube、B站等等的github上的开源项目。

在GPT搜索了一阵子以后，就会给你推荐一个，在github上，几乎封神的项目。

![](https://pbs.twimg.com/media/G_J_QqgaoAEc3Np.jpg)

它叫做，yt-dlp。

github上143k的star，说是真神，也不为过。

![](https://pbs.twimg.com/media/G_J9KOjX0AE5wTS.png)

支持上千个网站。

![](https://pbs.twimg.com/media/G_J-SxjXQAAgkSE.jpg)

这，就是yt-dlp，我觉得最伟大的项目之一。

你要相信，在这个世界上，在这个互联网上，有无数的大神和前人，已经为你铺好了前路。

你要相信，你的需求，永远不是这个世界上第一个提出这个需求的人，也绝对不是最后一个。

你要相信，人类在这几十年所积攒的历史，几乎覆盖了世界所有的领域，互联网，永远都是那个最深、最广的宝藏。

你要相信，在这一刻，你搜出来这个开源项目的这一刻，这就是人类开源精神的涓涓长河，在你面前展开的绝美的画卷。

我时常赞美这世界上，每一个愿意开源、每一个无私的将自己的知识分享出来的前辈们，正是因为他们，才让我们，能站在他们的肩上，去摘更美的星辰。

我们直接复制yt-dlp的github链接。

然后把这段Promtp发给你装好了skill-creator的OpenCode或者Claude Code：



帮我把这个开源工具：https://github.com/yt-dlp/yt-dlp

打包成一个Skill，只要我后续给出视频链接，就可以帮我下载视频。



这块如果还不懂或者不知道skill-creator是啥的，可以去看我之前的那篇文章：一文带你看懂，火爆全网的Skills到底是个啥。

一般我的做法是，先让Agent进行规划，然后再去写整个的Skill，这样我自己感觉，成功率会高一点、后期稳定性也会更强一点。

相对应的，OpenCode就是开启Plan模式。

![](https://pbs.twimg.com/media/G_J9hNraYAAL0gY.png)

然后，Agent就会开始调用skill-creator这个生成器，开始分析yt-dlp这个项目，然后开始规划要怎么打包封装成一个Skill。

![](https://pbs.twimg.com/media/G_J_DPfaoAEWuSN.jpg)

规划了一通以后，OpenCode就分析完了，向我提出了几个问题。

我也给出了我的回答。

![](https://pbs.twimg.com/media/G_J9to9aoAc5LLV.png)

然后它就会继续规划，最终给我一个非常明确的计划。

![](https://pbs.twimg.com/media/G_J8RtCaoAEX3ST.png)

我觉得没有问题了，这个时候，我就会切换到正式的开发模式。

也就是这个模式，然后发一句话，开始开发！

![](https://pbs.twimg.com/media/G_J9N9ebQAA0KHq.jpg)

OpenCode就会开始了。

过了一会，大概2分钟以后，这个基于yt-dlp的视频下载Skill，就开发完成了。

![](https://pbs.twimg.com/media/G_J-MMgXIAAIAEe.png)

我们试一试。

比如OpenAI刚刚出的Youtube访谈视频，我想下载下来。

![](https://pbs.twimg.com/media/G_J8leeaoAMqMk4.jpg)

直接就把链接扔给OpenCode就行，这里可以注意一个小技巧，就是所有的涉及到这种需要运行程序的Skills，在第一次运行的时候，都无脑推荐在OpenCode里使用GPT 5.2 Codex（如果你有的话），体验会比Claude 4.5 Opus好N倍。

大概就是：构建Skills的时候Claude 4.5 Opus，如果这些开源项目封装好了，在第一次运行的时候用GPT 5.2 Codex，后续就无所谓了。

![](https://pbs.twimg.com/media/G_J7wRIaoAI5VxQ.jpg)

第一次运行，其实会遇到很多问题，比如说Youtube防爬机制很强，需要你装个浏览器扩展导出Cookie，比如要安装一些其他的项目等等，不过这些AI都会指导你干好。

![](https://pbs.twimg.com/media/G_J9wnAa0AA1O8v.jpg)

然后一顿操作，这个项目，就下载好了，全程大概也就几分钟。

![](https://pbs.twimg.com/media/G_J9ldkakAAC9xn.jpg)

之所以是几分钟，还是因为，这是第一次。

而后续，只需要，十几秒。

这时候，其实你还可以做一个事，就是，把前面的那些为了下载视频而做的一些事情和经验，直接跟AI说：

把这些经验，都更新到video-downloader这个skill里，下次就别这么慢了。

然后，它就会自己对他的Skill文件进行修改，下次，这些事情，就不用干了，随开随下，快到起飞。

![](https://pbs.twimg.com/media/G_J7mLHXsAA0gNV.png)

这就是我的自己纯为了自己方便的一个skill全流程：

根据一个需求，用AI搜索github上的开源项目，把开源项目使用AI进行Skill化，首次运行后，寻找BUG和问题，重新迭代Skill，至此，Skill固化，形成我的主Agent中一个可靠的技能。

不止是一个下载视频的需求。

还可以是，把一个web项目，打包成一个轻量级的桌面APP。

![](https://pbs.twimg.com/media/G_J-ImsaoAITHR1.png)

于是，找到了Pake。

![](https://pbs.twimg.com/media/G_J73fXaMAA0lsd.jpg)

Github上一个45k的超棒的项目，那就，直接Skill化，以后，你的网页开发完，直接就可以用Pake skill，一句话变成桌面APP。

你还可以，直接做一个究极万能的格式转化工厂。

![](https://pbs.twimg.com/media/G_J90H6aoAEDih1.jpg)

直接把这些最牛逼的格式转化项目，直接封装在一起，做成一个万能的格式转化Skill。

从此，你无需各种奇怪的格式转化器，一个skill，解决所有。

你还可以，把ArchiveBox转成Skill，从此，你有想保存下来的网页，都可以发送给ArchiveBox Skill来以无数种你想要的格式，帮你保存下来。

支持N种格式，真的。

![](https://pbs.twimg.com/media/G_J8yuuaoAMMRs3.jpg)

甚至，你可以把著名的Ciphey，转成一个Skill。

从此，你就可以，在你的本地，配合Agent，直接破译密码。。。

![](https://pbs.twimg.com/media/G_J7_rEaAAAtnwW.jpg)

这些，全部都可以Skill化，全部都可以加入到你的Agent之中，成为，你最坚实的技能，成为，你最恐怖的弹药库。

而我提到的这些，仅仅只是Github上开源项目的冰山一角。

Github上牛逼的开源项目，那些人类的经验、人类的光芒。

本就灿烂如星海。

因为Skills的诞生，因为Agent的强大，现在，每个人、每个普通人，你的背后，都是全人类过去数十年的积累，只要你想，他就可以为你所用。

你无需三头六臂，你无需头上长角，你已经拥有了海量的知识和技能。

如果回到3年前的你的面前，你觉得，他跟你如今可以做到的事、如今的能力边界，还有任何可比性吗？

朋友，这样璀璨、这样伟大、这样能让你成为超人的时代。

真的不会让你兴奋吗？
---

---
url: "https://x.com/frxiaobei/status/2013888729463816414"
requested_url: "https://x.com/i/status/2013888729463816414"
author: "凡人小北 (@frxiaobei)"
author_name: "凡人小北"
author_username: "frxiaobei"
author_url: "https://x.com/frxiaobei"
tweet_count: 1
---

## 1
https://x.com/frxiaobei/status/2013888729463816414

推荐一个 cg33 @chg80333 的浏览器自动化项目：BrowserWing。

核心思路很顺，把网站能力直接转成 Skill。

基本把三个老大难一次性捋顺了，
1. 自动化太工程化
2. AI 自动点网页不稳定
3. AI 工具之间的集成割裂

MCP 和 Skills 原生支持这一点很关键，录完的流程导出直接塞进常用的 AI 工具继续用，复用和迁移成本都很低。

适合的场景我随手列几个：
电商比价和信息抓取
后台数据巡检
表单批量操作
用 AI 做半自动 RPA
需要登录态和 Cookie 稳定维持的任务

https://t.co/yowNTDZC8S
---

---
url: "https://x.com/Remotion/status/2013626968386765291"
requested_url: "https://x.com/i/status/2013626968386765291"
author: "Remotion (@Remotion)"
author_name: "Remotion"
author_username: "Remotion"
author_url: "https://x.com/Remotion"
tweet_count: 2
---

## 1
https://x.com/Remotion/status/2013626968386765291

Remotion now has Agent Skills - make videos just with Claude Code!

$ npx skills add remotion-dev/skills

This animation was created just by prompting 👇 https://t.co/hadnkHlG6E

![video](https://pbs.twimg.com/amplify_video_thumb/2013626156570877952/img/b4adUEB8w0C1nIX4.jpg)
[video](https://video.twimg.com/amplify_video/2013626156570877952/vid/avc1/1080x700/uqJ_M_PNHHPt190d.mp4?tag=21)

## 2
https://x.com/Remotion/status/2013628043105890779

Here's how we created the above video!

Full prompt history: https://t.co/OhyuqqsD0o https://t.co/h1T4JwCIKS

![video](https://pbs.twimg.com/amplify_video_thumb/2013627948209688576/img/kM_5h7aFhv5UNOrd.jpg)
[video](https://video.twimg.com/amplify_video/2013627948209688576/vid/avc1/1920x1080/sueKmjZJoURU6-JX.mp4?tag=21)
---

---
url: "https://x.com/LLMJunky/status/2013295156158480891"
requested_url: "https://x.com/i/status/2013295156158480891"
author: "am.will (@LLMJunky)"
author_name: "am.will"
author_username: "LLMJunky"
author_url: "https://x.com/LLMJunky"
tweet_count: 1
---

## 1
https://x.com/LLMJunky/status/2013295156158480891

I'm creating a list of skills that i use regularly. I have more to add but I have so many little projects going on.

My favorite new one is the ability to launch subagents in Codex. I just finished it!

I created an installer to make it easy for you to install!

These are my favorite three right now. More coming.

https://t.co/Qe0mxwCsfZ

![](https://pbs.twimg.com/media/G_CpLK7W4AEQR-U.jpg)
---

---
url: "https://x.com/LLMJunky/status/2013002697654284582"
requested_url: "https://x.com/i/status/2013002697654284582"
author: "am.will (@LLMJunky)"
author_name: "am.will"
author_username: "LLMJunky"
author_url: "https://x.com/LLMJunky"
tweet_count: 3
---

## 1
https://x.com/LLMJunky/status/2013002697654284582

Introducing Subagents for Codex - as a skill!

While we wait for the official release of Codex Subagents (they are coming), I created an intelligent skill that will automatically be called in your session any time a request is likely to 'waste' a significant number of tokens in the intermediate steps.

In other words, it should invoke itself any time a token hungry task is being launched where you only care about the final output.

Things like:
- Extensive file search in your codebase
- Web searching
- Long running tasks
- Documentation generation
- Multi Step Workflows
- Writing long form content
- Test suite analysis
- Log error analysis
- Migration and Refactoring
- Dependency Audits
- API exploration

And to take it a little further, any task that doesn't require additional intelligence (like web search or simple file exploration), Codex 5.1 Mini is used to save usage.

If its a multi step workflow that requires intelligence, it will inherit the parent's model/reasoning. Or the agent/user can change the model/reasoning if you choose. But if its just searching, it'll use 5.1 mini.

You may invoke this skill but it should work on its own.

I'm not the first or the last to think of something like this, but my aim here was to make it as simple as possible to implement it right into your existing Codex installation. 

Feedback welcome.

OSS Codex Skill Installer Available: https://t.co/Qe0mxwCsfZ

npx @am-will/codexskills --user am-will/codex-skills/skills/codex-subagent

![](https://pbs.twimg.com/media/G--ZalFXoAEdLVZ.png)

## 2
https://x.com/LLMJunky/status/2013006599716036921

Note: Turn on Background Terminal for this to work by typing /experimental in Codex CLI https://t.co/PZ9UI8zinS

![](https://pbs.twimg.com/media/G--i1RpWkAA2eSs.jpg)

## 3
https://x.com/LLMJunky/status/2013165310988243329

I made some updates to improve reliability this evening so if you downloaded it yesterday, please pull a fresh version. its much better now.
---

---
url: "https://x.com/AppSaildotDEV/status/2012503743569285305"
requested_url: "https://x.com/i/status/2012503743569285305"
author: "AppSail (@AppSaildotDEV)"
author_name: "AppSail"
author_username: "AppSaildotDEV"
author_url: "https://x.com/AppSaildotDEV"
tweet_count: 1
---

## 1
https://x.com/AppSaildotDEV/status/2012503743569285305

Vercel @andrewqu 这个 skills 妙啊

有点人工智能技能领域的“npm” 的意思了，好奇他们是怎么得到这个 package 的

安装命令：npx skills https://t.co/GM0uFGJDd4

![](https://pbs.twimg.com/media/G-3YXFzbgAA6xhZ.jpg)
---

---
url: "https://x.com/AxtonLiu/status/2010143669668720825"
requested_url: "https://x.com/i/status/2010143669668720825"
author: "Axton (@AxtonLiu)"
author_name: "Axton"
author_username: "AxtonLiu"
author_url: "https://x.com/AxtonLiu"
tweet_count: 2
---

## 1
https://x.com/AxtonLiu/status/2010143669668720825

我把 Obsidian 可视化三件套 Skills 开源了：

Canvas / Excalidraw / Mermaid

视频正在路上，几小时后上线，我会把：

- 官方 json-canvas vs 我的生成策略（含 Mindmap / Freeform）
- Excalidraw / Mermaid 实测
- 安装路径 等等都演示一遍。 https://t.co/6pO7jMZAwF

![](https://pbs.twimg.com/media/G-V3AePasAEvMvT.jpg)
![](https://pbs.twimg.com/media/G-V3ArZasAQp5l1.jpg)
![](https://pbs.twimg.com/media/G-V3A7JaoAADtUT.jpg)

## 2
https://x.com/AxtonLiu/status/2010143682322972774

Repo 地址：

https://t.co/CWwjzy74qJ
---

---
url: "https://x.com/dotey/status/2009540783255261559"
requested_url: "https://x.com/i/status/2009540783255261559"
author: "宝玉 (@dotey)"
author_name: "宝玉"
author_username: "dotey"
author_url: "https://x.com/dotey"
tweet_count: 2
---

## 1
https://x.com/dotey/status/2009540783255261559

推荐王老师的教程，另外刚才测试了一下王老师写的自动发布 X 文章的 Skill，真的是强大，而且给我很大启发，理论上来说基于这个思路可以做一个发布微信公众号或者其他平台的 Skill。

原理是用脚本控制浏览器，用剪贴板把文字和图片粘贴到编辑器，最有创意的是，根据文字定位到图片要插入的位置👍

> Author: Wang Shuyi (@wshuyi)
> URL: https://x.com/wshuyi/status/2009451186039214388
>
> https://t.co/UP5hKcQO1B

## 2
https://x.com/dotey/status/2009541037425938521

王老师发布 X 文章的 Skill：
https://t.co/TQsUbLy8Sb
---

---
url: "https://x.com/vista8/status/2009809828823306354"
requested_url: "https://x.com/i/status/2009809828823306354"
author: "向阳乔木 (@vista8)"
author_name: "向阳乔木"
author_username: "vista8"
author_url: "https://x.com/vista8"
tweet_count: 1
---

## 1
https://x.com/vista8/status/2009809828823306354

如何从零用Claude agent SDK搭建一个智能体。

有160多万阅读。

作者的substack也发了，先Mark。

除了Skill，下一个很值得研究的就是Agent SDK。

https://t.co/OWccfct0Sp

> Author: nader dabit (@dabit3)
> URL: https://x.com/dabit3/status/2009131298250428923
>
> https://t.co/PqGEcSahx8
---

---
url: "https://x.com/QingQ77/status/2009516554036396417"
requested_url: "https://x.com/i/status/2009516554036396417"
author: "Geek Lite (@QingQ77)"
author_name: "Geek Lite"
author_username: "QingQ77"
author_url: "https://x.com/QingQ77"
tweet_count: 1
---

## 1
https://x.com/QingQ77/status/2009516554036396417

三天，2.6k 星标……疯了

obsidian-skills 是由 Obsidian 的首席执行官 Steph Ango 开发的一个开源项目，旨在为 Anthropic 的 AI 助手 Claude 提供直接操作 Obsidian 笔记库的能力。

你只需要把这堆代码扔进你笔记库的 /.claude 文件夹里，就这么简单。

https://t.co/HzvcAbR7yr
---

---
url: "https://x.com/LinearUncle/status/2009514546617307452"
requested_url: "https://x.com/i/status/2009514546617307452"
author: "LinearUncle (@LinearUncle)"
author_name: "LinearUncle"
author_username: "LinearUncle"
author_url: "https://x.com/LinearUncle"
tweet_count: 3
---

## 1
https://x.com/LinearUncle/status/2009514546617307452

这个obsidian的canvas skill真心好用，用来画各种精美的图形。
在Claude Code安装后，使用slash command唤醒，提示词：
```/json-canvas 画一个精美的思维导图，主题是：如何致富
```
https://t.co/tQ1FtUU5Bu

安装教程：
1. 在你的obsidian vault目录下创建一个.claude目录
2. 从github仓库里下载obsidian-skills解压到.claude目录
3. 把目录名改成skills,也就是.claude/skills
4. 在你的obsidian vault目录下启动claude code

> Author: 向阳乔木 (@vista8)
> URL: https://x.com/vista8/status/2009138313618477105
>
> Claude Code 安装Obsidian CEO 写的一个Skill ：Canvas
>
> 安装后提问：
>
> “你先搜索清朝的皇帝和故事，画一个canvas？”
>
> 可视化学习真棒啊，效果如下： https://t.co/k3PTdCoNYt

![](https://pbs.twimg.com/media/G-M56xNWsAELGRe.jpg)

## 2
https://x.com/LinearUncle/status/2009515724331725164

查看了SKILL. md文件，核心原理就是把Obsidian Canvas的语法用例子仔细讲解了一遍，从而AI就掌握了在Obsidian Canvas上画图的语法。 https://t.co/RzjXMRckQU

![](https://pbs.twimg.com/media/G-M7uAvawAAPTdS.jpg)

## 3
https://x.com/LinearUncle/status/2009518664488505390

这个skill用来画代码视图也挺好用 https://t.co/Dp8IZls4h5

![](https://pbs.twimg.com/media/G-M-fn3awAAwbpd.jpg)
---

---
url: "https://x.com/JefferyTatsuya/status/2009847151153820103"
requested_url: "https://x.com/i/status/2009847151153820103"
author: "Jeffery Kaneda　金田達也 (@JefferyTatsuya)"
author_name: "Jeffery Kaneda　金田達也"
author_username: "JefferyTatsuya"
author_url: "https://x.com/JefferyTatsuya"
tweet_count: 1
---

## 1
https://x.com/JefferyTatsuya/status/2009847151153820103

更新了 skill-from-masters ⬆️

之前只从本地数据库找方法论，现在加了三层搜索：

- 本地数据库
- 联网搜专家和框架
- 深挖原始资料（访谈、演讲、文章）

还加了：
- 自动搜"黄金样例"——看看最好的输出长什么样
- 自动搜"常见错误"——把反面教材也编进去
- 交叉验证多个来源，找共识、标分歧

目标：不是"能用"，是达到人类顶级水平。

🔗 https://t.co/CnGXbiFBSf

> Author: Jeffery Kaneda　金田達也 (@JefferyTatsuya)
> URL: https://x.com/JefferyTatsuya/status/2009109135766507602
>
> Skill谁都能写，高品质的Skill很难写。
>
> 难在哪？
> 不是格式，不是语法——
> 是你根本不知道这件事的最佳做法是什么。
>
> 但其实，大部分领域早有大师把方法论说透了：
> 乔布斯讲产品、讲招聘、讲营销，
> 马斯克讲第一性原理，
> 贝佐斯讲Day 1和六页备忘录，
> 芒格讲多元思维模型。
>
> 他们花几十年踩坑，你直接抄答案。
>
> 所以我写了 skill-from-masters：
> 创建Skill前，先帮你找到这个领域的大师框架，
> 选好方法论，再生成Skill。
>
> 品质不是写出来的，是选出来的。
>
> 🔗 https://t.co/CnGXbiFBSf
---

---
url: "https://x.com/vista8/status/2009673263442735252"
requested_url: "https://x.com/i/status/2009673263442735252"
author: "向阳乔木 (@vista8)"
author_name: "向阳乔木"
author_username: "vista8"
author_url: "https://x.com/vista8"
tweet_count: 1
---

## 1
https://x.com/vista8/status/2009673263442735252

安装superpowers 这个牛逼的Claude 插件。

然后跟Claude 说，调用skill帮我把下面文章变成Skill。

一个思考框架Skill就写好了。

1.5w Star的Claude 插件安装地址。
https://t.co/qeEj48W1UK

> Author: 向阳乔木 (@vista8)
> URL: https://x.com/vista8/status/2009671866613649691
>
> https://t.co/wazSKCUCm0

![](https://pbs.twimg.com/media/G-PKywIbYAEg5qa.jpg)
---

---
url: "https://x.com/Yangyixxxx/status/2009223364590616684"
requested_url: "https://x.com/i/status/2009223364590616684"
author: "Yangyi (@Yangyixxxx)"
author_name: "Yangyi"
author_username: "Yangyixxxx"
author_url: "https://x.com/Yangyixxxx"
tweet_count: 2
---

## 1
https://x.com/Yangyixxxx/status/2009223364590616684

ai这个时代是真的魔幻

头部在晒元skills以及寻找knowhow提升ai效果的最佳实践
极客在用各种skills产出东西
自媒体在用skills获得流量卖社群卖课
倒爷在搜索skills聚合卖信息差
小红书评论区在问什么是skills
公司老板在问怎么订阅claude
公司员工在研究翻墙与信用卡

23年到26年
转眼3年了
agi没有来 
但中转站和薅羊毛的号贩子全发家致富了

信息在爆炸
但人与人差距的初始就藏在上下文里
人和动物最大的差别是人会使用工具
我不记得这个定义是谁下的
但我觉得人和人最大的差别
也是使用工具

如果你要问是使用什么工具
最底层的 大概是搜索工具

## 2
https://x.com/Yangyixxxx/status/2009224112275902600

可能不止人
AI应该也是

你的claudecode和我的claudecode
为什么都是claudecode
却做出来的千差万别的效果

有些vibecoding是蓝绿tailwind css
有些vibecoding却是高级品味的设计风范

能力也藏在搜索上啊
因为一个ai搜索到了优秀的上文
一个没有

仅此而已
---

---
url: "https://x.com/wshuyi/status/2009451186039214388"
requested_url: "https://x.com/i/status/2009451186039214388"
author: "Wang Shuyi (@wshuyi)"
author_name: "Wang Shuyi"
author_username: "wshuyi"
author_url: "https://x.com/wshuyi"
tweet_count: 4
---

# Claude Skills 入门：一篇文章搞懂 AI 怎么从「嘴替」升级成「打工人」

![](https://pbs.twimg.com/media/G-L20T3XcAAZ4eB.jpg)

你有没有这种感觉 ——AI 领域的新名词，比手机型号更新还快？

昨天刚搞懂「函数调用」(Function Calling) 是怎么回事，今天又冒出来个「Skills」。前天有人跟你说「MCP」，你还没反应过来，后天又有人聊「Agent」。每次看到这些词，第一反应都是：我是不是又落伍了？

别慌。今天咱们把「Claude Skills」这事儿掰开揉碎了讲清楚。

更重要的是，我会告诉你它跟你已经知道的那些概念 —— 函数、函数调用 —— 到底是什么关系。你会发现，这不是三个孤立的新词，而是一层一层往上搭的台阶。搞懂这三层，以后再出什么新词，你也能自己判断它在哪一层。

## 起点

咱们从最熟悉的东西开始：编程里的「函数」。

你可以把函数理解成一个「小助手」。你告诉它要做什么（给它一个输入），它帮你做完后告诉你结果（给你一个输出）。就像餐厅里的服务员：你点菜，他端菜，每次都按照固定流程来。

举个例子，程序员写一个叫 `calculate_tax (income)` 的函数。你把收入数字扔进去，它把该交多少税算出来还给你。下次还要算？再调用一遍就行。不用每次都重写一遍算税的逻辑。

函数的价值，说白了就三个字：封装、重用、标准化。

把一件事情的做法「打包」起来，以后谁都能用，每次用的方式都一样。这是程序员几十年来最基本的生产力工具。

![](https://pbs.twimg.com/media/G-L4pI3WUAACQ6n.jpg)

但函数有个局限 —— 它只活在代码世界里。

程序员在代码里写 `getWeather()`，这个函数 100% 会被执行。可是普通人不会写代码，AI 也不会直接「运行」这些代码。那怎么让 AI 也能用上这些「小助手」呢？

## 架桥

2023 年前后，一个叫「函数调用」（Function Calling）的概念火了起来。

你可以把它理解成：给那个「只会聊天的 AI」配了一部电话和一本通讯录。

以前的 AI，你问它「今天北京天气怎么样」，它要么从训练数据里瞎猜一个，要么老老实实说「我不知道」。因为它没有「手脚」，不能真的去查天气。

有了函数调用之后，情况变了。

开发者事先告诉 AI：「这是一本通讯录，里面有个叫 `get_weather` 的函数，你想查天气就打这个电话。」AI 收到「今天北京天气怎么样」的问题后，它会自己判断：「哦，这个问题我得打电话给 `get_weather` 才能回答。」

然后它生成一段标准格式的「便签」（叫 JSON），上面写着：

> {
>   "function": "get_weather",
>   "arguments": {
> "city": "北京"
>   }
> }

这段便签被外部程序接收、解析、执行。真正打电话给气象台的，是外部程序，不是 AI 自己。执行完后，结果返回给 AI，AI 再用人话告诉你：「北京今天晴，15 度。」

这里有个关键的转折，初学者容易忽略。

传统函数是「确定性」的——程序员在代码里写了 `getWeather()`，100% 会执行。

但 LLM 的函数调用是「概率性」的——AI 看到「今天天气怎么样」，它要自己判断该不该调用天气函数。这个判断是基于理解，不是基于规则。有小概率它会判断错误，比如把「天气」理解成某个人名。

所以说，函数调用的本质是：让 AI 能「打电话」，但打不打、打给谁，它自己决定。

这是一个巨大的进步 ——AI 不再只是「知识库」，它开始变成「行动者」。

![](https://pbs.twimg.com/media/G-L5iWgW8AAiyG6.jpg)

但函数调用还有个问题：它是零散的、一次性的。

你给 AI 配了十几个函数，它每次只能选一个打电话。如果一个任务需要连续调用五六个函数、中间还有逻辑判断、还需要参考一些文档，函数调用就不够用了。

## 跃升

2025 年 10 月 16 日，Anthropic 发布了一个新功能：Claude Skills。

你可以把 Skills 理解成「员工手册」+「工具箱」的组合。

员工手册告诉 AI：「当你遇到某类任务时，应该怎么做，分几步，每一步用什么工具。」工具箱里装着它需要用的脚本和参考资料。

具体来说，一个 Skill 就是一个文件夹，里面有三样东西：

第一，SKILL.md 文件。这是「指令」，用自然语言写的。告诉 AI：这个 Skill 是干什么的，什么情况下该用，怎么用，有什么注意事项。

第二，脚本。可以是 Python、JavaScript 或者其他语言写的代码。当 AI 需要「动手」的时候，就执行这些脚本。

第三，资源文件。比如参考文档、模板、配置文件。AI 在执行任务的时候可以查阅这些资料。

你可能会问：这跟函数调用有什么本质区别？

区别在于：函数调用是「单个工具」，Skills 是「整套解决方案」​。

打个比方。函数调用像是给你一把锤子、一把螺丝刀、一把扳手，你得自己知道什么时候用哪个。Skills 像是给你一本《如何组装宜家书柜》的说明书，说明书里不仅告诉你步骤，还附上了所有需要的工具和零件。

还有一个重要的机制叫「渐进式披露」。

AI 的「工作记忆」是有限的（技术上叫「上下文窗口」）。如果你把所有 Skills 的内容一股脑塞进去，AI 会被信息淹没。

Skills 的做法是：平时只告诉 AI「有这么一本说明书」，AI 真正需要的时候再去翻。就像你不用把整本百科全书背下来，遇到问题再查相关那一页就行。

![](https://pbs.twimg.com/media/G-L3NNRWAAAYaoz.jpg)

现在，咱们把三层放在一起看：

![](https://pbs.twimg.com/media/G-L6QRTW0AAtfzD.jpg)

从下往上看，抽象层次越来越高。函数是代码级的，函数调用是接口级的，Skills 是工作流级的。

Skills 可以包含函数调用，但函数调用只是 Skills 的一部分。

就像一本菜谱不只是「切菜」「炒菜」「装盘」这几个动作的罗列，它还包括「为什么要这样做」「火候怎么掌握」「如果烧焦了怎么补救」这些知识。

## 实战

说了这么多概念，Skills 到底能干什么？咱们看几个真实案例。

先说一个我自己的项目：x-article-publisher-skill。

![](https://pbs.twimg.com/media/G-L3sgkWMAAJGwr.jpg)
![](https://pbs.twimg.com/media/G-L43HPW8AAUt3e.jpg)

如果你用 Markdown 写文章，然后想发布到 X（Twitter）的 Articles 功能里，你会遇到一个极其崩溃的问题：复制粘贴过去，格式全丢了。

标题变普通文字，粗体变普通文字，链接变普通文字。你得手动一个一个加回来。一篇文章，光是调格式就要花 15-20 分钟。

更要命的是图片。你得手动上传每一张，然后把它拖到正确的位置。如果文章有十几张图，你很容易搞错顺序。

这个 Skill 怎么解决的呢？

它会先解析你的 Markdown 文件，提取标题、封面图，并且给每张内容图片计算一个「块索引」（block_index）—— 就是这张图应该出现在文章的第几个段落之后。

然后，它把 Markdown 转成富文本 HTML，通过剪贴板粘贴到 X 编辑器里。格式完美保留。

最后，它用浏览器自动化（Playwright）把每张图片精准插入到正确的位置。

原本 20-30 分钟的手动操作，现在几分钟内全自动搞定。减少时长自不必说。对懒人而言，能全程不用自己再动手，才是最主要的嘛。

你可能会说：这不就是写了个自动化脚本吗？

是，也不是。

单纯的自动化脚本，你得自己记住什么时候用、怎么用、参数怎么填。但 Skill 把「什么时候用」「怎么用」都写进了指令里。你只需要跟 AI 说一句「把这篇文章发到 X」，它就知道该调用这个 Skill，该怎么操作。

这就是「知识编码」的价值——把「我知道怎么做」变成「AI 也知道怎么做」。

再看几个企业场景。

会议管理：有个 Skill 能自动从会议记录里提取摘要、决策和行动项，然后起草跟进邮件。开完会不用再花半小时整理笔记。

数据分析：扔给它一个 CSV 文件，它能自动识别关键指标、找出异常值，生成图文并茂的报告。非技术人员也能快速从数据里挖出洞察。

客户支持：它从公司知识库里检索准确答案，再用人性化的语言组织成回复。既保证准确，又不失温度。

这些场景有个共同点：都是重复性高、步骤固定、但又需要一定判断力的任务。以前，要么靠人硬扛，要么花大价钱开发专门的软件。现在，一个 Skill 就能搞定。

最后说说开发者工具。

有个叫 `skill-creator` 的 Skill，特别有意思 —— 它是用来创建 Skill 的 Skill。

![](https://pbs.twimg.com/media/G-L5XpNXQAAw35c.jpg)

你跟它聊天，告诉它你想实现什么工作流，它会帮你生成一个完整的 Skill 项目框架。这就是所谓的「元技能」。

还有 `webapp-testing`，能根据测试用例自动操作浏览器，对 Web 应用进行功能测试，然后生成测试报告。前端测试流程部分自动化了。

## 动手

说了这么多，怎么开始用 Skills？

如果你想用现成的 Skills，最简单的方式是通过 Claude Code 的插件市场。

默认初始自动安装的只是 Claude 官方的插件市场。

你也可以根据自己的需求，添加其他插件市场。格式例如：

> /plugin marketplace add anthropics/claude-code

安装之后，你这里就有两个插件市场了。

![](https://pbs.twimg.com/media/G-L4eR-WwAASYi-.jpg)

你看到了，利用 `/plugin` 命令，可以添加、管理插件。

这是我目前已经安装的部分插件。

装完之后，你可以让 Claude 用某个 Skill 来完成任务。比如：「用 PDF Skill 提取这份文件里的表格数据。」

如果你想自己创建 Skills，可以用 `skill-creator` 这个元技能。跟它对话，描述你的工作流，它会帮你生成框架。

你可以编写 Claude Skill，让它帮助你去分析材料、自动调研，并且绘制出对应的结构图。

例如这是红楼梦人物关系图。

下面是战国七雄的互动。

使用方式可以 参考我这篇文章。

![](https://pbs.twimg.com/media/G-L5M0jXAAApqJv.jpg)

更高级的玩法是用 Claude Skills 连接一些非常好的外部工具，例如 NotebookLM 作为知识库使用。这样你就可以把 NotebookLM 强大的检索和知识验证功能，与你自己的创意以及其他模型工具的特点有机地结合在一起。

![](https://pbs.twimg.com/media/G-L3Vn0XcAAfUAb.jpg)

我在 这篇文章当中有详细的介绍。

![](https://pbs.twimg.com/media/G-L6FxcWcAAZufc.jpg)

想看看别人做了什么 Skills？去 GitHub 搜 awesome-claude-skills，那里有社区整理的优秀 Skill 清单。

![](https://pbs.twimg.com/media/G-L60Z9XYAAy8sV.jpg)

我个人比较推荐的是活水智能（也就是阳志平老师团队）做的 插件市场 42plugin 。

![](https://pbs.twimg.com/media/G-L3FyFXUAAmUBV.jpg)

这里不仅整理了很多的插件，而且还有相应的评级评分，更可以保证避免踩坑。

最重要的一点：创建 Skill 不一定需要会写代码。

SKILL.md 里的指令是自然语言写的。如果你的工作流不涉及复杂的脚本，光靠自然语言指令就能完成很多事情。

正如 Claire Vo 在 Lenny's Newsletter 里说的：即使是非程序员，也可以通过清晰地定义工作流，创建出强大的、可复用的 AI 工作流。

![](https://pbs.twimg.com/media/G-L7CmQW0AAkUVK.jpg)
![](https://pbs.twimg.com/media/G-L3eOyXQAAMxPT.jpg)

## 小结

现在咱们回头看这三层台阶：

- 编程函数是基石。它提供了最基础、最可靠的逻辑执行单元。
- LLM 函数调用是桥梁。它让 AI 不再只是「知识库」，而是能「打电话」驱动外部世界的行动者。
- Claude Skills是蓝图。它把零散的工具和指令整合成完整的工作流，让 AI 能更可靠、更专业地完成复杂任务。

这三层会越来越融合。开发者继续写高效的函数作为底层工具；通过函数调用把工具暴露给 AI；再用 Skills 指导 AI 怎么智能地使用这些工具。

真正的力量在于：它让「领域专家」也能「教」AI。

你不需要是程序员，只需要清楚自己的工作流程是什么，就能把这些知识打包成一个 Skill。你的专业知识不再只存在于你脑子里，它变成了 AI 可以调用的能力。

对了，就在我写这篇文章的时候（2026 年 1 月 8 日），Claude Code 又发布了一次重大更新。Skills 现在支持隔离上下文、热重载、指定模型、在子代理中使用……Plugin Marketplace 也正式上线了。

Anthropic 还把 Agent Skills 规范作为 开放标准 发布 —— 这跟他们之前推 MCP（Model Context Protocol）的路数一样，都是走开放生态路线。

![](https://pbs.twimg.com/media/G-L3lr2WEAAyOmu.jpg)

Gartner 的分析师说，这标志着 AI 市场的焦点正在从「模型更新」转向「用例落地」。

翻译成人话就是：大家不再只比谁的模型更聪明，而是开始比谁能把 AI 用得更好。

Skills 是这场转变的核心载体。它让 AI 从「应答者」变成了「协作者」。

下次再有人跟你说什么关于 Agent 功能的新词，你就问自己：它是在哪一层？是代码级的工具，是接口级的桥梁，还是工作流级的蓝图？

想清楚这个，新词就不再可怕了。

你有没有尝试过 Claude Skills？有没有自己制作符合你自己工作流的 Claude Skill？

欢迎分享在留言区，咱们一起交流讨论。

## 延伸阅读

- 品味还是技能？ChatGPT 引发的能力培养变革
- AI 时代的真稀缺技能：从「有技术」到「会洞察」
- 如何用 Claude Skill 帮你一句话做深度调研并自动画图？
- 从枯燥理论到生动实践：AI 智能代理如何用交互式教程讲解复杂概念
- 新学期，给你自己配一个好用的 AI 助手吧。会思考，能联网，还有知识库那种

## Media

![](https://pbs.twimg.com/media/G-L6bveXMAA3vgQ.jpg)
![](https://pbs.twimg.com/media/G-L5tI9XMAAALwG.jpg)

## Thread

### 1
https://x.com/wshuyi/status/2009897950416404695

当你真的开始创建并且迭代自己的 AI 技能时，很快就会遭遇到一个问题：改错了之后，没有「后悔药」。于是我又做了一个 Claude Skill，帮你给技能迭代增加版本快照，随时一声令下回退。分享给你，解决你的后顾之忧。https://t.co/VTcWddu824

> Author: Wang Shuyi (@wshuyi)
> URL: https://x.com/wshuyi/status/2009896989912117327
>
> https://t.co/o2fQuzBRtE

### 2
https://x.com/wshuyi/status/2010353411666108649

小说「当产品经理遇到 Claude Skills」：https://t.co/JGd3XdKW4w

> Author: Wang Shuyi (@wshuyi)
> URL: https://x.com/wshuyi/status/2010352847964209183
>
> https://t.co/jKp5XdGrtr

### 3
https://x.com/wshuyi/status/2014144232186118181

解答星友疑惑，对几个相关概念做了讲解和辨析：

> Author: Wang Shuyi (@wshuyi)
> URL: https://x.com/wshuyi/status/2013940553281683588
>
> https://t.co/Vaa4axdNm6
---

---
url: "https://x.com/wshuyi/status/2006174274436907389"
requested_url: "https://x.com/i/status/2006174274436907389"
author: "Wang Shuyi (@wshuyi)"
author_name: "Wang Shuyi"
author_username: "wshuyi"
author_url: "https://x.com/wshuyi"
tweet_count: 2
---

# 如何用 Claude Skill 将 Markdown 图文无痛发布 X Premium 文章？

![](https://pbs.twimg.com/media/G9dbwQuXgAALN2E.jpg)

## 痛点

你有没有过这种崩溃的时刻？

在 Obsidian 或者 VS Code 里，你行云流水地写完了一篇洋洋洒洒的 Markdown 文章。逻辑通顺，配图完美，甚至连代码块都高亮得恰到好处。你满怀期待地按下 `Cmd+C`，打开 X (Twitter) 的 Articles 页面，按下 `Cmd+V`。

然后，悲剧发生了。

所有的标题变成了普通文本，精心标注的加粗消失了，代码块乱作一团。你不得不叹一口气，把鼠标变成了「缝纫机」——选中标题，点击 H1；选中重点，点击加粗；遇到链接，还得一个个重新复制粘贴。

最绝望的是图片。如果你的文章里有 10 张图，在 X Articles 里意味着你要点击「添加媒体」-「选择文件」-「等待上传」整整 10 次。如果你想把图片精准地插在某两段文字中间，还得在编辑器里小心翼翼地滚动寻找光标位置。

因为 X 编辑器默认你在这里是码字。如果出现图，也应该是在它专门提供插图的地方插入。

而在文章当中，出现图的概率「应该并不高」，所以你遇到有图片地方再插入就好。

可惜我的风格不是这样的。我一般喜欢做教程，教程里的图可能是写几个段落就得用一张图作为佐证或者说明。这样的话，我一篇文章最多可能有 40 多张图。

一篇高质量的长文，写作可能只花了 1 小时，但在这个「格式化地狱」里排版，可能就要耗掉你好几十分钟，且被编辑器搞得心烦意乱。这不仅仅是时间的浪费，更是对创作心流的粗暴打断。

为了解决这个问题，我写了一个 Claude Skill 工具：X Article Publisher Skill。

它不搞虚头巴脑的「黑科技」，只做一件事：把你的 Markdown 稿件，完美地「填」进 X 的编辑器里。

## 演示

在这个工具的帮助下，流程变成了这样：

你只需要对着 Claude 说一句：「把这篇文章发布到 X」，然后给出 markdown 文件链接即可。

接下来的 几分钟 里，你可以喝口水，看着屏幕上的浏览器自动打开，封面图自动上传，标题自动填写。最神奇的是，它会像变魔术一样，瞬间把带有 H1、H2、粗体、链接、列表的富文本内容「注入」到编辑器中。

紧接着，它会根据你 Markdown 里的位置，精准地把每一张插图「塞」进对应的段落之间。

一切就绪后，它会停在「保存草稿」这一步。

从 20 分钟的机械劳动，到几分钟的自动化操作。 这就是我想带给你的体验。

## 原理

你可能会问，这背后的原理是什么？

首先，我们利用 Python 脚本，将你的 Markdown 解析并转换为 HTML 富文本，然后通过系统剪贴板，一次性将「骨架」注入编辑器。这样做的好处是，所有的格式（粗体、标题、链接）都能被 X 编辑器完美识别，而且速度极快，稳如泰山。

骨架搭好后，我们再利用 Playwright 自动化技术，像做填空题一样，通过锚点定位，把图片一张张精准地填入它们该去的位置。

这就是为什么它能兼顾速度与准确。

## 门槛

虽然这个工具能带来「10 倍效率」的提升，但我必须诚实地告诉你，它不是给所有人准备的。它有一定的使用门槛。

首先，它是一个「硬核玩家」的玩具。你需要准备好 Claude Code ，以及一些依赖库。当然了，如果 Claude Code 已经配置好，这些依赖库也可以喊 Claude Code 为你安装。

其次，它目前仅支持 macOS。因为我们在实现「剪贴板注入」这一核心功能时，使用了 `pyobjc` 库来调用 macOS 的底层接口。Windows 用户如果直接运行，会因为缺少这个库而报错。如果你是 Windows 上的 Python 高手，欢迎通过替换 `pywin32` 来帮我们完善它。

最后，默认前置条件，你需要是 X Premium Plus 订阅用户。因为只有这个级别的订阅，X 才开放 Articles（长文）功能。

如果你符合以上条件，那么恭喜你，你将获得一套极致的发布工作流。

## 上手

如果你决定尝试，请按照以下步骤配置。

第一步：检查权限

确认你已经是 X Premium Plus 用户，并且在 Chrome 浏览器中已经登录了 X 账号。执行的时候它会开启一个新的 Chrome 窗口，你在这里面可能需要重新登录一遍。

第二步：安装 Claude Code

此处从略。

第三步：安装 Skill

你可以通过 Git 将工具克隆到本地，然后配置到你的 Claude 或其他 MCP 客户端中。



或者，你也可以使用插件市场。

第四步：开始发布

在 Claude 中，使用自然语言指令：

> 帮我把 `~/Documents/my-best-article.md` 发布到 X。

然后，保持弹出的 Chrome 浏览器窗口可见（不要最小化），看着它自动替你完成那些枯燥的工作。

## 承诺

作为一个辅助工具，我必须向你明确它的边界。

第一，绝不自动发布。

工具的最后一步永远是「保存草稿」。为了安全起见，最终的检查权和发布按钮，必须掌握在人类（也就是你）的手中。你可以预览效果，确认无误后，再亲手点击发布。

第二，关于维护。

这是一个基于网页自动化（Playwright）的工具，它强依赖于 X 网页版的代码结构。如果下周 X 的前端工程师修改了一个 `div` 的类名，这个脚本可能就会失效。

请把它看作是一个实验性的项目。如果它报错了，请不要惊慌，欢迎在 GitHub 上提 Issue，或者自己（请 Claude Code ）动手修补它——毕竟，这才是极客精神所在，不是吗？

## 小结

X Article Publisher Skill 的初衷，是践行 DRY (Don't Repeat Yourself) 原则。

在这个 AI 时代，我们的时间应该花在思考和创作上，而不是花在选中文字、点击加粗这种重复的一百次的机械操作上。

希望这个小工具，能帮你找回写作和分享的纯粹乐趣。

## 延伸阅读

- AI 工作流长文写作能力重大改进，欢迎你来试试看
- AI 时代，请停止「做作业」，去创造属于你的「作品」
- 如何用Markdown轻松排版知乎专栏文章？
- 未来的写作长啥样？LEX 用 GPT-3 AI 给你点儿颜色看看
- 从高亮到输出：如何用 Readwise 一站式优化你的阅读笔记流程？

## Media

![](https://pbs.twimg.com/media/G9dcEYLXcAEnfPx.jpg)

## Thread

### 1
https://x.com/wshuyi/status/2009452074795454745

看很多小伙伴对 Claude Skill 神奇能力很感兴趣，但是不知道如何入门，于是我又写了一篇 Claude Skill 入门教程：https://t.co/bTe5qIpiSM

> Author: Wang Shuyi (@wshuyi)
> URL: https://x.com/wshuyi/status/2009451186039214388
>
> https://t.co/UP5hKcQO1B
---

---
url: "https://x.com/rohanpaul_ai/status/2009277278048637145"
requested_url: "https://x.com/i/status/2009277278048637145"
author: "Rohan Paul (@rohanpaul_ai)"
author_name: "Rohan Paul"
author_username: "rohanpaul_ai"
author_url: "https://x.com/rohanpaul_ai"
tweet_count: 1
---

## 1
https://x.com/rohanpaul_ai/status/2009277278048637145

Some interesting way to use Claude Skills

---

Claude Skills teach Claude how to complete specific tasks in a repeatable way

So Skills are just folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. 

A skill can package prompts + tools (APIs, files, Model Context Protocol servers, etc.) into a reusable workflow with a name/description (and usually some YAML config). Then you just invoke it in chat like: “Run Document Suite on this draft” or “Use Webapp Testing on /login”.

![](https://pbs.twimg.com/media/G-JgdlWaoAAz9Ty.png)
---

---
url: "https://x.com/shao__meng/status/2009434025052733828"
requested_url: "https://x.com/i/status/2009434025052733828"
author: "meng shao (@shao__meng)"
author_name: "meng shao"
author_username: "shao__meng"
author_url: "https://x.com/shao__meng"
tweet_count: 1
---

## 1
https://x.com/shao__meng/status/2009434025052733828

10 个真正改变我工作方式的 Claude Skills

Reddit/ClaudeAI 中看到的帖子，作者总结了自己持续测试后真正觉得有价值的 10 个 Skills，聚焦于提升生产力、自动化和专业输出，涵盖开发、文档、设计、测试等场景。

1. Rube MCP Connector
通过一个统一的 MCP 服务器，将Claude一次性连接到 500+ 应用（Slack、GitHub、Notion 等），无需为每个应用单独配置认证。适合需要大量自动化集成的用户，大幅节省时间。

2. Superpowers（obra 开发的开发者工具包）
提供 /brainstorm、/write-plan、/execute-plan 等专用命令，将 Claude 从普通聊天机器人转变为完整的开发工作流辅助工具。对严肃编码的人来说是重大提升。

3. Document Suite（Anthropic 官方 Skills）
让 Claude 真正擅长处理和创建 Word、Excel、PowerPoint、PDF 文件，支持正确格式、公式等，而不仅仅是读取。处理客户发来的复杂文件时特别实用。

4. Theme Factory
一次性上传品牌指南（颜色、字体等），之后 Claude 生成的所有 Artifacts 都会自动遵循该风格。非常适合营销团队保持品牌一致性。

5. Algorithmic Art
基于 p5.js 的生成艺术工具，只需文字描述（如“蓝紫渐变流场，5000 个粒子，种子 42”），即可生成可复现的艺术作品。适合创意编码者。

6. Slack GIF Creator
直接根据描述生成专为 Slack 优化的自定义动画 GIF，无需再去 Giphy 搜索。实用且有趣的小工具。

7. Webapp Testing
使用 Playwright 自动化框架，描述测试需求（如“测试登录流程”），Claude 就能编写并运行测试脚本。QA 工程师和开发者会觉得特别好用。

8. MCP Builder
快速生成自定义 MCP 服务器的样板代码，将搭建集成的时间缩短约80%。适合自己开发 Skills 或复杂集成的用户。

9. Brand Guidelines
与 Theme Factory 类似，但支持同时管理多个品牌风格，并轻松切换。适合需要处理不同品牌项目的团队。

10. Systematic Debugging
让 Claude 按资深工程师的思路系统化调试：找出根本原因 → 提出假设 → 提供修复方案 → 编写文档。避免了以往“瞎猜式”调试。

上面这 10 个 Skills 的资源地址：
https://t.co/I9PkD8H203
https://t.co/NQAZtNz2Hr
https://t.co/kvVX3wQLUN
https://t.co/lAZLuGHZ2G

> Author: Rohan Paul (@rohanpaul_ai)
> URL: https://x.com/rohanpaul_ai/status/2009277278048637145
>
> Some interesting way to use Claude Skills
>
> ---
>
> Claude Skills teach Claude how to complete specific tasks in a repeatable way
>
> So Skills are just folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks.
>
> A skill can package prompts + tools (APIs, files, Model Context Protocol servers, etc.) into a reusable workflow with a name/description (and usually some YAML config). Then you just invoke it in chat like: “Run Document Suite on this draft” or “Use Webapp Testing on /login”.

![](https://pbs.twimg.com/media/G-LxkbzboAEr98L.jpg)
---

---
url: "https://x.com/vista8/status/2009138313618477105"
requested_url: "https://x.com/i/status/2009138313618477105"
author: "向阳乔木 (@vista8)"
author_name: "向阳乔木"
author_username: "vista8"
author_url: "https://x.com/vista8"
tweet_count: 1
---

## 1
https://x.com/vista8/status/2009138313618477105

Claude Code 安装Obsidian CEO 写的一个Skill ：Canvas

安装后提问：

“你先搜索清朝的皇帝和故事，画一个canvas？”

可视化学习真棒啊，效果如下： https://t.co/k3PTdCoNYt

> Author: 向阳乔木 (@vista8)
> URL: https://x.com/vista8/status/2008714622035956104
>
> Obsidian CEO写的Skill，基于X用户调研。
>
> 这几天，他好像经常问大家用给Ob写了什么好玩的Claude Skill。
>
> 其实，大家的回复更精彩，但他写的很基础底层。
>
> ① 写出Obsidian风格的Markdown （内链、属性等）
> ② 生成.Base 文件的过滤器和公式
> ③ 生成Canva无限画布等
>
> 用这个很简单，只需要告诉Claude Code：
>
> 安装这里的skills  https://t.co/QlNfzOHoDR

![](https://pbs.twimg.com/media/G-HkL0SakAAKghb.jpg)
---

---
url: "https://x.com/vista8/status/2009049757109637364"
requested_url: "https://x.com/i/status/2009049757109637364"
author: "向阳乔木 (@vista8)"
author_name: "向阳乔木"
author_username: "vista8"
author_url: "https://x.com/vista8"
tweet_count: 1
---

## 1
https://x.com/vista8/status/2009049757109637364

必装Claude Skill之 planning-with-files

作者Ahmad Othman Ammar Adi。

看 Manus 被20亿美元收购，参考Manus的Agent方法写的Skill

很适合多步骤任务，用这个Skill指导其他Skill工作也挺好。

AI也需要有计划性，写TodoList，完成Check，不止于遗忘和跑偏。

安装很简单，只需要跟Claude说

“安装这个Claude Skill：https://t.co/uTeedTyZKK”

![](https://pbs.twimg.com/media/G-GR58cakAE4SoN.jpg)
![](https://pbs.twimg.com/media/G-GSH1Wa0AATHTy.jpg)
---

---
url: "https://x.com/JefferyTatsuya/status/2009109135766507602"
requested_url: "https://x.com/i/status/2009109135766507602"
author: "Jeffery Kaneda　金田達也 (@JefferyTatsuya)"
author_name: "Jeffery Kaneda　金田達也"
author_username: "JefferyTatsuya"
author_url: "https://x.com/JefferyTatsuya"
tweet_count: 1
---

## 1
https://x.com/JefferyTatsuya/status/2009109135766507602

Skill谁都能写，高品质的Skill很难写。

难在哪？
不是格式，不是语法——
是你根本不知道这件事的最佳做法是什么。

但其实，大部分领域早有大师把方法论说透了：
乔布斯讲产品、讲招聘、讲营销，
马斯克讲第一性原理，
贝佐斯讲Day 1和六页备忘录，
芒格讲多元思维模型。

他们花几十年踩坑，你直接抄答案。

所以我写了 skill-from-masters：
创建Skill前，先帮你找到这个领域的大师框架，
选好方法论，再生成Skill。

品质不是写出来的，是选出来的。

🔗 https://t.co/CnGXbiFBSf
---

---
url: "https://x.com/godofprompt/status/2008578110141190580"
requested_url: "https://x.com/i/status/2008578110141190580"
author: "God of Prompt (@godofprompt)"
author_name: "God of Prompt"
author_username: "godofprompt"
author_url: "https://x.com/godofprompt"
tweet_count: 2
---

# 🔑 you can just build skills

![](https://pbs.twimg.com/media/G9_ltM0W0AQzCCQ.jpg)

3 months ago I was writing the same prompts over and over.

Today I have systems that run entire decision frameworks, generate content in my exact voice, and guide me through complex problems step by step.

The shift happened when I stopped treating Claude like a chatbot and started treating it like a team member who needs onboarding.

Most people don't realize Claude now has a feature that completely changes how you interact with it. It's called Skills. And if you're creating content, engineering prompts, or solving complex problems, ignoring this is leaving serious leverage on the table.

Here's everything you need to actually use it.

## > what skills actually are (and why most people get it wrong)

Everyone thinks Skills are just fancy system prompts. Wrong.

Skills are portable instruction packages that teach Claude your specific workflows. Think of them as onboarding documents for an AI. You write the instructions once. Claude loads them automatically whenever they're relevant.

The structure is dead simple:

skill-name/
├── SKILL.md        (required - your instructions)
├── scripts/        (optional - executable code)
├── references/     (optional - docs Claude can read)
└── templates/      (optional - files for output)

## > how to enable Skills

1. Navigate to Settings > Capabilities.
2. Ensure that Code execution and file creation is enabled.
3. Scroll to the Skills section.
4. Toggle individual skills on or off as needed.
5. To add custom skills, click "Upload skill" and upload a ZIP file containing your skill folder.

![Claude Skills example](https://pbs.twimg.com/media/G9_l65DW8AQahcM.jpg)

One markdown file with YAML frontmatter at minimum. Everything else is optional.

Here's the mental model that changed everything for me: if you've typed the same prompt more than five times, you should have built a Skill by now.

## > the skill-creator skill (your shortcut to building anything)

Here's what most people miss: Claude already has a built-in skill called skill-creator that builds skills for you.

You don't need to understand file structures. You don't need to write YAML. You just describe what you want.

Important: Don't assume Claude will automatically load the skill. Be explicit.

Type this exactly: "Use the skill-creator skill to create a skill for [your workflow]"

Examples:

- "Use the skill-creator skill to create a skill for writing LinkedIn posts in my voice"
- "Use the skill-creator skill to create a skill for analyzing competitor pricing"
- "Use the skill-creator skill to create a skill for weekly report generation"
- "Use the skill-creator skill to create a skill for code documentation"

When you invoke it explicitly, Claude asks clarifying questions. What's your process? What are the steps? Show me examples. What should the output look like?

Then it generates the folder structure, writes the SKILL.md, and packages everything into a downloadable file. You upload it to Settings > Capabilities > Skills. Done.

This is genuinely the fastest way to get started. I still use it for rapid prototyping.

## > pro tip: let claude research your business and create a context profile

This might be the most underrated technique.

You can have Claude perform deep research on your business, website, or personal data and extract everything into a structured context profile. Then save that profile as a skill.

Here's how:

- Enable "Research" mode in Claude
- Tell Claude: "Research my website [URL] and extract a comprehensive context profile including: business model, target audience, value propositions, tone of voice, key products/services, competitive positioning, and any unique terminology or frameworks I use."
- Or: "Analyze these documents I'm uploading and create a complete business context profile I can reuse."
- Or: "Based on our conversation history, extract everything you know about my business, preferences, and working style into a structured profile."

Claude will dig through your website, documents, or conversation history and compile a detailed context file.

Save that output as a skill:

---
name: my-business-context
description: Complete context profile for [Your Business] including business model, audience, voice, products, and terminology. Load this when creating any content or making strategic decisions.
---

## Business Overview
[Claude's extracted summary]

## Target Audience
[Detailed audience profile]

## Products/Services
[Complete offerings breakdown]

## Brand Voice
[Tone, style, banned phrases]

## Key Terminology
[Industry terms, internal language, frameworks]

## Competitive Position
[Market positioning, differentiators]

Now you never explain your business again. Every conversation starts with Claude already knowing who you are, what you sell, how you talk, and who you serve.

This works for:

- Business context (website, pitch decks, about pages)
- Personal brand (your content history, voice patterns)
- Project context (documentation, repos, requirements)
- Client profiles (for agencies handling multiple clients)

One research session. Permanent context. Zero repeated explanations.

## > turning prompts into skills (the obvious move nobody makes)

Here's the unlock most people miss.

That mega-prompt you've been copying and pasting? That detailed system instruction you refined over 20 iterations? That's already a skill. You just haven't packaged it yet.

The conversion is simple:

1. Take your working prompt
2. Add YAML frontmatter at the top (name + description)
3. Save as SKILL.md
4. Upload to Claude

---
name: your-skill-name
description: Clear description of what this does and when Claude should use it
---

[Your existing prompt goes here]

That prompt you perfected for writing LinkedIn posts? Now it loads automatically whenever you mention LinkedIn content. The system prompt you use for code review? Now Claude uses it every time you share code.

Stop copying. Start converting.

## > powerful example: the problem-solver skill

Let me show you what a serious skill looks like.

I built a problem-solver skill that transforms Claude into an elite strategic consultant. Not a surface-level "here are some tips" assistant. A rigorous analytical framework.

The skill has 8 interconnected modules:

1. First Principles Breakdown (strip problem to fundamental truths)
2. Root Cause Analysis (5 Whys technique)
3. SCQA Framework (Situation, Complication, Question, Answer)
4. Game Theory Analysis (player incentives, Nash equilibria, strategic positioning)
5. Second-Order Consequences (what happens after what happens)
6. Design Thinking (human-centered solutions)
7. OODA Loop (Observe, Orient, Decide, Act)
8. Solution Synthesis (integrated action plan)

Each module has specific questions Claude must answer. Each module ends with "Type 'continue' when ready."

The description in my SKILL.md:

---
name: problem-solver-skill
description: Elite problem-solving system using first principles thinking, game theory, critical analysis, and systematic frameworks to solve complex business challenges
---

To use it, I say: "Use the problem-solver skill to help me think through [business challenge]"

Claude doesn't give me generic advice. It walks me through a Pentagon-level analytical framework. It asks clarifying questions. It maps player incentives. It calculates strategic positions. It identifies second and third-order consequences.

That's the difference between a chatbot and a system.

## > pro tip: skills can ask questions back

This is the technique that makes skills actually useful.

Instead of dumping everything at once, design your skill to guide the user through phases.

Example from my content skill:

## Phase 1: Content Type Selection

What type of content do you need?

1. X Article (long-form single post)
2. X Thread (multi-tweet sequence)
3. X Giveaway (comment [keyword] format)
4. X Quote (quoting another post)
5. X Prompt Post (steal my prompt format)

Reply with the number.

The user types "2" and Claude proceeds to the thread-specific workflow.

Or use open-ended phase progression:

### Module 1: Problem Understanding

Before we proceed, I need to understand your situation completely.

What specific challenge are you facing?
Who are the key players involved?
What outcomes are you hoping to achieve?

Ready for the next module? Type "continue"

This does three things:

1. Prevents Claude from assuming and getting it wrong
2. Forces the user to think through their actual needs
3. Creates a conversation flow instead of a wall of text

Design skills like dialogues, not documents.

## > skills that run your entire workflow

Here's where this gets interesting.

Skills aren't limited to answering questions. They can run entire decision processes.

Email writing skill example:

---
name: email-composer
description: Write professional emails matching my voice and communication style
---

## Workflow

Phase 1: Gather context
- Who is the recipient?
- What's the relationship (colleague, client, cold outreach)?
- What's the goal of this email?
- What tone is appropriate?

Phase 2: Draft structure
- Opening line (no "I hope this finds you well")
- Core message (one main point)
- Call to action (specific, clear)
- Sign-off (match formality level)

Phase 3: Generate and refine
- Write draft
- Check for passive voice
- Remove filler phrases
- Ensure CTA is explicit

## My Voice Guidelines
- Direct but warm
- Short paragraphs (2-3 sentences max)
- No corporate speak
- Always end with clear next step

## Banned Phrases
- "I hope this finds you well"
- "Per my last email"
- "Just circling back"
- "Touching base"

Now when I say "use the email-composer skill to write an email to [person] about [thing]," Claude doesn't guess. It asks the right questions, follows my structure, uses my voice, avoids my banned phrases.

Strategic decision skill example:

Your skill can embed entire decision frameworks. My problem-solver skill includes game theory analysis where Claude:

- Identifies all players and their incentives
- Maps available actions for each party
- Calculates Nash equilibria
- Identifies dominant strategies
- Develops counter-strategy responses

This isn't Claude giving opinions. It's Claude running a systematic analytical process and showing its work.

## > the architecture that makes this efficient

Skills use progressive disclosure. This is the key insight.

Claude doesn't load all your instructions immediately. It works in layers:

- Layer 1: Claude scans metadata (~100 tokens). Just the name and description to figure out what's relevant.
- Layer 2: If a Skill applies, Claude loads the full instructions (<5k tokens).
- Layer 3: Scripts, templates, and reference files only load when Claude actually needs them.

This means you can have 20+ Skills available without overwhelming Claude's context window. The system is designed for composability.

Pro tip: If Claude isn't loading a skill automatically, invoke it explicitly: "Use the [skill-name] skill to [task]"

This guarantees the skill loads and runs.

## > composable skills: the power move

Skills stack. You can have multiple focused skills active simultaneously.

Example setup for content creation:

- my-business-context skill: Your extracted business profile
- brand-voice skill: Your tone, banned phrases, style patterns
- research-workflow skill: How to gather and verify information
- x-content skill: Platform-specific formatting rules

When you ask Claude to write an X thread about a topic, it can load all four skills and combine their instructions.

Build modular expertise instead of monolithic prompts.

## > the context window is a public good

This mindset shift separates good Skills from bloated ones.

Every token in your Skill is a token not available for the actual conversation. Default assumption: Claude is already smart. Only add what it doesn't know.

Before adding any instruction, ask:

- Does Claude really need this explanation?
- Does this paragraph justify its token cost?
- Is this genuinely non-obvious?

Prefer concise examples over verbose explanations. If your SKILL.md approaches 500 lines, split it into multiple files.

My problem-solver skill is 580 lines. That's at the upper limit. It works because each module is discrete and Claude only processes relevant sections.

## > practical workflow for building your first serious skill

Week 1: Identify your high-value repetitive tasks

List every prompt you've copy-pasted in the last month. Which ones took the most iteration to get right? Which ones do you use most frequently?

Pick the one with highest (frequency × complexity).

Week 2: Document your actual process

Before writing SKILL.md, write out your process as if explaining to a new hire:

- What questions do you need answered first?
- What are the steps in order?
- What does good output look like?
- What mistakes should be avoided?

Week 3: Build the skill using skill-creator

Tell Claude: "Use the skill-creator skill to create a skill for [your process]"

Walk through the questions. Let it generate the structure. Download and upload.

Week 4: Test on real tasks and iterate

Use the skill on actual work. Notice where Claude gets it wrong. Update the instructions. Add examples. Clarify ambiguous sections.

Within a month you'll have a system that multiplies your output.

## > real examples of skills worth building

For content creators:

- Business context profile (extracted from your website/docs)
- Brand voice skill (tone, banned phrases, formatting rules)
- Platform-specific skills (X threads, LinkedIn posts, newsletters)
- Research and fact-checking workflow
- Content repurposing (video → thread → article)

For prompt engineers:

- Prompt structure templates (XML, JSON, markdown formats)
- Evaluation frameworks (how to assess prompt quality)
- Iteration workflows (systematic improvement process)

For business:

- Decision frameworks (like my problem-solver skill)
- Email composition (voice-matched, situation-appropriate)
- Meeting prep (agenda generation, pre-read summaries)
- Report generation (structured analysis, consistent formatting)
- Client context profiles (for agencies with multiple clients)

For developers:

- Code review workflow
- Documentation generation
- Bug analysis framework
- Architecture decision records

## > quick reference: how to invoke skills

Don't assume Claude loads skills automatically. Be explicit for best results:

- "Use the skill-creator skill to create a skill for [task]"
- "Use the problem-solver skill to analyze [challenge]"
- "Use the email-composer skill to write an email about [topic]"
- "Use the brand-voice skill when writing this content"
- "Use my-business-context skill for this project"

Pattern: "Use the [skill-name] skill to [action]"

This guarantees the skill activates.

## > the takeaway

You don't need to write the same prompts forever.

You don't need to re-explain your business every conversation.

You don't need Claude guessing what you want.

Skills let you teach Claude once and benefit indefinitely.

Start here:

1. Have Claude research your business/website and extract a context profile
2. Save that profile as your first skill
3. Use skill-creator skill to build workflow-specific skills
4. Design interactive phases that ask the right questions
5. Stack skills for complex workflows
6. Always invoke skills explicitly for guaranteed activation

Build the system. Then watch what happens when Claude actually knows how you work.

If you're building content systems or decision frameworks, follow me. I break down the workflows that actually scale.

Drop your most repetitive task in the comments. I'll tell you how I'd structure the skill.

You can just build skills.

Subscribe to my newsletter for weekly AI prompts & workflows.

🔑 God of Prompt

## Thread

### 1
https://x.com/godofprompt/status/2008640531744911829

Your premium AI bundle to 10x your business

→ Prompts for marketing &amp; business
→ Unlimited custom prompts
→ n8n automations
→ Pay once, own forever

Grab it today 👇
https://t.co/C8Zzw2Jkpc
---

---
url: "https://x.com/godofprompt/status/2008590835131281894"
requested_url: "https://x.com/i/status/2008590835131281894"
author: "God of Prompt (@godofprompt)"
author_name: "God of Prompt"
author_username: "godofprompt"
author_url: "https://x.com/godofprompt"
tweet_count: 1
---

## 1
https://x.com/godofprompt/status/2008590835131281894

Claude Skills is the best feature I’ve ever used.

Here's how I use them (and how you can too) 👇

> Author: God of Prompt (@godofprompt)
> URL: https://x.com/godofprompt/status/2008578110141190580
>
> https://t.co/rPdSjVH7ky
---

---
url: "https://x.com/shao__meng/status/2008707651409244169"
requested_url: "https://x.com/i/status/2008707651409244169"
author: "meng shao (@shao__meng)"
author_name: "meng shao"
author_username: "shao__meng"
author_url: "https://x.com/shao__meng"
tweet_count: 1
---

## 1
https://x.com/shao__meng/status/2008707651409244169

[开源推荐] Obsidian Skills for Claude Code

Obsidian CEO @kepano 开源了 obsidian-skills，针对 Claude Code 等的 “Skills” 集合，专为 Obsidian 用户设计。核心目的是让 Claude Code 等更好地理解、创建和编辑 Obsidian 知识库中的特定文件格式，提升 Claude Code 等在 Obsidian 生态中的辅助能力。

主要功能和特点  
项目提供了三项专属 Skills，支持 Obsidian 的独特文件类型：  
· obsidian-markdown：处理 Obsidian 增强型 Markdown 文件，包括维基链接、嵌入、呼出框和前端属性等语法。  
· obsidian-bases：支持 Obsidian 的 Bases 功能，允许 Claude 处理过滤器、公式和汇总等数据库式操作。  
· json-canvas：处理 Obsidian 的 Canvas 文件，这是一个无限画布格式，支持节点、边和分组的 JSON 结构。  

这些 Skills 会自动为 Claude 提供相关的语法指导、模式文档、最佳实践建议，以及 Bases 公式的完整函数参考，帮助 Claude Code 等更准确地生成或修改 Obsidian 内容，而不会出现格式错误。

工作原理  
当用户在 Claude Code 中处理 Obsidian vault 文件时，这些 Skills 会自动激活，为 AI 注入 Obsidian 专属上下文知识。用户可以将 Obsidian vault 与 Claude 结合使用，让 AI 直接编辑笔记、创建数据库视图或构建画布，而无需手动解释 Obsidian 的专有语法。

开源地址
https://t.co/SVREj6Faf1

> Author: kepano (@kepano)
> URL: https://x.com/kepano/status/2008578873903206895
>
> I'm starting a set of Claude Skills for Obsidian... so far they're centered around helping Claude Code edit .md, .base, and .canvas files
> https://t.co/vQWtoGjoxv

![](https://pbs.twimg.com/media/G-Bc9JqbcAU9gYO.jpg)
---

---
url: "https://x.com/eze_is_1/status/2008732184748978663"
requested_url: "https://x.com/i/status/2008732184748978663"
author: "一泽Eze (@eze_is_1)"
author_name: "一泽Eze"
author_username: "eze_is_1"
author_url: "https://x.com/eze_is_1"
tweet_count: 4
---

## 1
https://x.com/eze_is_1/status/2008732184748978663

全网最好的  agent skill 终极中文指南，全文 1.2w 字，终于写完了，欢迎收藏与讨论！

从基础概念、应用价值优势，
到使用与制作教程、哪些场景适合做 skill
都给了说人话的详尽解析。

结合了不同复杂度的 skill 实验与多篇技术博客后，我把我对 Skills 的完整应用思考写成了这篇长文。

巧借通用 Agent 内核，只靠 Skills 设计，就能低成本创造具有通用 AI 智能上限的垂直 Agent 应用。

![https://mp.weixin.qq.com/s/jUylk813LYbKw0sLiIttTQ](https://pbs.twimg.com/media/G-BzAY8bcAAotoT.jpg)
![](https://pbs.twimg.com/media/G-BzCD5agAA-deg.jpg)

## 2
https://x.com/eze_is_1/status/2008732381860294923

Skill 和 MCP 有什么区别？

MCP 是一种开放标准的协议，关注的是 AI 如何以统一方式调用外部的工具、数据和服务，本身不定义任务逻辑或执行流程。
Skill 则教 Agent 如何完整处理特定工作，它将执行方法、工具调用方式以及相关知识材料，封装为一个完整的「能力扩展包」，使 Agent 具备稳定、可复用的做事方法。

以 Anthropic 官方 Skills 为例：

PDF：包含  PDF 合并、拆分、文本提取等代码脚本，教会 Agent 如何处理 PDF 文件 - 提取文本，创建新的 PDF、合并或拆分文档。
Brand-guidelines：包含品牌设计规范、Logo 资源等，Agent 设计网站、海报时，可参考 Skill 内的设计资源，自动遵循企业设计规范。
Skill-Creator：把创建 Skill 的方法打包成元 Skill，让 AI 发起 Skill 创建流程，引导用户创建出符合需求的高水准 Skill。

但 Skills 的价值上限，远不止于此。

它应该是一种极其泛用的新范式，从垂直 Agent 到 AI 产品开发：借用通用 Agent 内核，0 难度创造具备通用 AI 智能的垂直 Agent 应用。

## 3
https://x.com/eze_is_1/status/2008732563117142229

Skills 相较于它的前辈们（Workflow 和程序编写的 AI 应用）有了 3 个关键优势：

1)非技术人员可用零代码、自然语言编写
2)能突破预设限制，灵活响应用户输入，应对边缘情况
3)甚至能多个 Skill 自由联用，应用方式极其灵活

## 4
https://x.com/eze_is_1/status/2008732659217047653

原文地址：https://t.co/f8CmZG0njZ
---

---
url: "https://x.com/PMbackttfuture/status/2008514348810203625"
requested_url: "https://x.com/i/status/2008514348810203625"
author: "AI产品黄叔 (@PMbackttfuture)"
author_name: "AI产品黄叔"
author_username: "PMbackttfuture"
author_url: "https://x.com/PMbackttfuture"
tweet_count: 1
---

## 1
https://x.com/PMbackttfuture/status/2008514348810203625

用Skills一键解读论文

整个创意感谢@vista8 @servasyy_ai
我把乔木老师和huangserva发的两条推特信息
给到CC，让它进行调研
然后chat几轮后

整个Skills就出来了
对于调研和审美能力感到吃惊 https://t.co/eS9jfogAXy

![](https://pbs.twimg.com/media/G9-s_ctW4AAp1NV.jpg)
![](https://pbs.twimg.com/media/G9-tCobWMAEVX0f.jpg)
![](https://pbs.twimg.com/media/G9-tFnnWQAEDzWJ.jpg)

![video](https://pbs.twimg.com/amplify_video_thumb/2008511901114802176/img/7GoRHcmnVmy4Jepp.jpg)
[video](https://video.twimg.com/amplify_video/2008511901114802176/vid/avc1/1832x1080/rBMNWGf9NvQq9GeK.mp4?tag=21)
---

---
url: "https://x.com/servasyy_ai/status/2008076852683018485"
requested_url: "https://x.com/i/status/2008076852683018485"
author: "huangserva (@servasyy_ai)"
author_name: "huangserva"
author_username: "servasyy_ai"
author_url: "https://x.com/servasyy_ai"
tweet_count: 1
---

## 1
https://x.com/servasyy_ai/status/2008076852683018485

玩了一下乔木大佬的skills，非常好玩
我改了一下输出，除了md文件，还增加了PDF输出

找了一篇论文：https://t.co/cvBS8XOZhd

过程如图

生成的PDF效果（豆包做的图）：https://t.co/1AfPmTGEgh https://t.co/VlQjEwfT79

![](https://pbs.twimg.com/media/G94e_xbbgAAQDay.jpg)
![](https://pbs.twimg.com/media/G94e_xdbIAAavlC.jpg)
---

---
url: "https://x.com/YukerX/status/2008156911611633896"
requested_url: "https://x.com/i/status/2008156911611633896"
author: "Yuker (@YukerX)"
author_name: "Yuker"
author_username: "YukerX"
author_url: "https://x.com/YukerX"
tweet_count: 1
---

# 小白也能解锁 Claude Code 的秘密武器：Skills （附示例文档）

![](https://pbs.twimg.com/media/G95n-JKaEAAUOWT.jpg)

两个月以来，我一直在思考一个问题：该如何提升AI的能力呢？

哪怕有了CLAUDE.md，可以让他记住了我是谁，我喜欢什么；但我该如何让他学习到我的“能力”呢？

这就是我今天要说的主角 -- Skill 功能

这东西彻底改变了我对 AI 协作的看法。它不再是简单的“你问我答”，而是让 AI 主动学习、来配合你的能力和偏好。
这感觉就像，你不是在跟一个什么都懂的实习生说话，而是在跟一个资深团队成员协作。

Claude Code 虽然名字里带个 Code，但它绝不仅仅是写代码的工具。它是一个真正的通用 Agent，能帮你处理电脑上各种繁琐的工作。而 Skill，就是它能力无限扩展的“插件包”。

也就是说，他理论上可以很大程度的把我们每个人的能力“抽象”出来，形成一种可移植的“模块”。不论你是做市场的，还是做产品的，又或是做运营的，它都能帮到你。 

# 1. Skill 到底是什么？

> 简单来说，Skill 是一个“能力单元”，它把专业知识、工作流程和最佳实践打包起来，让 Claude Code 能够自动调用。

最关键的区别在于：你不需要像用斜杠命令（/command）那样手动触发它。CC 会根据对话上下文，自己判断什么时候该用哪个 Skill。
它就像一个有经验的同事，看到你在处理某个特定任务，会主动过来说：“这个我熟，我来帮你。”

Skills 可以根据你的需要，存储在不同位置，作用范围也不同：

想象一下：

- 对于个人：你可以把你最常用的代码片段、写作风格、数据分析流程，封装成个人 Skill。从此，Claude Code 就是最懂你的那个助手。
- 对于团队：团队的设计规范、API 使用指南、项目提交流程……这些都可以做成项目 Skill，放在代码仓库里共享。新成员加入，CC 自动就能带他上路，再也不需要一遍遍地人肉培训。

# 2. 如何“教会”你的 AI？--30秒上手 Skill 创建

听起来很复杂？恰恰相反。创建一个 Skill 非常简单，你只需要一个文件夹和一个 SKILL.md 文件。我这里带大家一步步拆解。

## 第一步：创建你的 Skill 目录

> 💡 团队协作首选项目 Skills，因为它们可以被检入 git，团队成员拉下代码就能自动获得新能力。

## 第二步：编写灵魂文件 SKILL.md

> 🫡完整的skills示例我将放到文章最后，想先有个框架思路的可以划到最后看一眼先。

这是 Skill 的核心，它由两部分组成：YAML frontmatter（元数据）和 Markdown（指令）。不用怕这些概念，他们很简单。

1️⃣命名的艺术

name 字段推荐使用英文，且动名词形式（动词 + -ing），让能力一目了然。
✅ 推荐: processing-pdfs, analyzing-spreadsheets, writing-documentation
❌ 避免：helper, utils, documents (过于模糊)

2️⃣真正的魔法：description

> description 字段是 Claude Code 能否“智能”激活你的 Skill 的关键。
> 它必须用第三人称清晰地描述“它能做什么”以及“什么时候用它”。

好的例子：

糟糕的例子：

描述越精确，包含的触发关键词越多（如 git diff, commit message），Claude Code 就越“懂你”。

3️⃣你甚至可以让 Claude Code 自己给你写一个skill

可以参考下列模板进行写作：

## 第三步：目录架构（⚠️大多数人倒在这里）

![](https://pbs.twimg.com/media/G95drtHbgAAs-Du.jpg)

这张图目前大家只需要关注三个部分：

1. 🗃️Skills：这个是在Claude目录中的skills文件夹
2. 🗃️my-skill：这是最多人容易出错的地方，所有SKILL.md文件，都需要放置在文件夹当中，否则Claude code识别不出来。
3. 📜SKILL.md : 这就是详细的skill文档，也就是我们上面在讲解的。

其余的文件这篇文章就先不讲述了，留在工作流篇章进行讲解，以保证文章的易读性。

这时候，当你再去Claude code里面输入 /skills 指令，就能够清晰的看到你的目录中有哪些skill是存在的。对，就这么简单！

# 3. 一个真实的用法：40秒，把 1000 条用户吐槽变成产品洞察

做产品的最怕版本发布后的前三天。
App Store 评论、客服后台的工单、社群里的吐槽像雪片一样飞来。以前我们得安排两个实习生，花一整天把这些反馈复制到 Excel 里，一条条打标签，最后统计出“这周大家到底在骂什么”，效率低且容易漏掉关键问题。

于是，我们创建了一个叫 feedback-analyst 的项目 Skill。

SKILL.md 的 description 写得非常清楚：

> description: 读取用户反馈或评论列表，进行情感分析，自动将其归类为“功能缺陷”、“体验优化”或“新需求”，并提取出现频率最高的 Top 5 痛点。当用户提供原始反馈数据并请求分析时使用。

现在，每当运营导出一份乱七八糟的反馈 CSV 文件，只需要对 Claude Code 说一句：“帮我看看这周用户的差评主要集中在哪”，CC 就会自动激活这个 Skill，瞬间读完几千字的内容，忽略掉无意义的情绪宣泄，直接告诉你：“60% 的差评是因为新上线的‘深色模式’导致文字看不清，建议优先修复。”

整个过程立竿见影，从前需要人肉分类一整天的工作，现在喝口水的时间就有了结论，决策有了真实的数据支撑。这只是冰山一角，你可以用它来分析竞品在 App Store 的差评（寻找机会点）、整理原本枯燥的用户访谈逐字稿、甚至从几十页的行业报告中提炼出关键趋势。

最重要的是，Skill 能把每个人的能力给抽象化成为一种模块组件；让这个组件可以在团队内部，甚至于外部进行流通。
🤔这也是为什么有人会质疑Claude借此来骗取专业人士的知识。

# 4. 结语：巨鲸潜行，万物生长

如果说之前的 AI 是一个无所不知的“巨鲸”，那 Skill 机制则让整个生态“万物生长”。

它把定义“能力”的权力，从 AI 公司交还给了每一位用户、每一个团队。我们不再只是被动的使用者，而是主动的“训练师”和“赋能者”。我们正在见证一个新时代的开启：AI 将不再是一个个孤立的“大脑”，而是能够深度融入我们工作流、理解我们独特上下文的“超级伙伴”。

如果你也想体验电脑上最智能的 AI，感受这种“人机合一”的默契，一定要试试 Claude Code 和它的 Skill 功能。

万事开头难，但这篇文章已经为你铺平了最开始的道路。当你遇到任何重复性的、繁琐的工作时，不妨打开 Claude code，跟它聊聊，或者干脆为它创建一个 Skill。

相信我，你很快会找到属于自己的“Aha Moment”！

# 5. 附录：一个Skill框架示例



## Media

![](https://pbs.twimg.com/media/G9498vOaYAAdFHX.png)
---

---
url: "https://x.com/leeoxiang/status/2008128859993207059"
requested_url: "https://x.com/i/status/2008128859993207059"
author: "Leo Xiang (@leeoxiang)"
author_name: "Leo Xiang"
author_username: "leeoxiang"
author_url: "https://x.com/leeoxiang"
tweet_count: 1
---

## 1
https://x.com/leeoxiang/status/2008128859993207059

这个 Skill 很有意思，用持续更新的 Markdown 来规划、跟进和沉淀知识，参考了 Manus 的实现。

看了这个 skill 之后很受启发：先做规划，但规划不是一次性的，而是在执行过程中持续更新和修正。
这种“持续思考、持续回写”的模式非常符合复杂任务，不过也意味着一次任务会经历很多轮理解和更新，对 token 的消耗会被进一步放大。

https://t.co/rkwbTYvLG1
---

---
url: "https://x.com/geekbb/status/2008038811616555394"
requested_url: "https://x.com/i/status/2008038811616555394"
author: "Geek (@geekbb)"
author_name: "Geek"
author_username: "geekbb"
author_url: "https://x.com/geekbb"
tweet_count: 1
---

## 1
https://x.com/geekbb/status/2008038811616555394

我不知道这是什么，但它在 GitHub 上冲得太快了

一个为 Claude Code 开发的技能（Skill），灵感来源于 Manus AI，通过持久化的 Markdown 文件来管理任务规划、进度追踪和知识存储。

根据项目描述，Meta 在 2025 年 12 月 29 日以 20 亿美元收购了 AI 代理公司 Manus。
Manus 之所以能在 8 个月内从发布做到 1 亿美元以上营收，核心秘诀在于“上下文工程”（Context Engineering）——即把 Markdown 文件当作磁盘上的“工作记忆”。

AI 在做任何重大决定前，会先读取 task_plan.md 以确保目标在注意力窗口内。每完成一个阶段，AI 会更新文件中的复选框状态。这种“文件系统即记忆”的模式，使得 AI 能够处理长达 50 次以上的工具调用而不迷失方向

https://t.co/AuEAWAaceO
---

---
url: "https://x.com/vista8/status/2007291809903550558"
requested_url: "https://x.com/i/status/2007291809903550558"
author: "向阳乔木 (@vista8)"
author_name: "向阳乔木"
author_username: "vista8"
author_url: "https://x.com/vista8"
tweet_count: 1
---

## 1
https://x.com/vista8/status/2007291809903550558

信息过载？写个工具每天只看真正值得的内容。

写了一个Claude Skill，每日抓取更新Newsletter，HN、producthunt的新内容。

9点推送一个整理好的文档，点击用Obsidian查看。

打✅ 说明阅读完了，删除。
打⭐️说明不错，自动归档。

后续可以让Skill自动把打星号的写成文章，选择性发公众号。

![](https://pbs.twimg.com/media/G9tUZk9asAgoakD.jpg)
![](https://pbs.twimg.com/media/G9tUdaXXkAANPRu.jpg)
![](https://pbs.twimg.com/media/G9tU_WnasAQuktx.jpg)
![](https://pbs.twimg.com/media/G9tVF-BbgAAfNaX.jpg)
---

---
url: "https://x.com/AsphaltCowb0y/status/2007674007106335199"
requested_url: "https://x.com/i/status/2007674007106335199"
author: "Jeremy Longshore (@AsphaltCowb0y)"
author_name: "Jeremy Longshore"
author_username: "AsphaltCowb0y"
author_url: "https://x.com/AsphaltCowb0y"
tweet_count: 2
---

## 1
https://x.com/AsphaltCowb0y/status/2007674007106335199

@xiaoerzhan Colabs included plus cli wizard to create your own skills plugin https://t.co/A0s87TPYac

## 2
https://x.com/AsphaltCowb0y/status/2007674211347935688

@xiaoerzhan Cli wizard 

https://t.co/3VBHV38eWO
---

---
url: "https://x.com/xiaoerzhan/status/2007315880905191603"
requested_url: "https://x.com/i/status/2007315880905191603"
author: "小耳👂Jane｜Xiaoer (@xiaoerzhan)"
author_name: "小耳👂Jane｜Xiaoer"
author_username: "xiaoerzhan"
author_url: "https://x.com/xiaoerzhan"
tweet_count: 2
---

## 1
https://x.com/xiaoerzhan/status/2007315880905191603

现在已经有一批现成的 Skills 聚合站，把全网高手的成果都摆在你面前，内容多、更新快、还有分类和搜索：

• https://t.co/3fR6mZz3GO
• https://t.co/BDixxs0WN9
• https://t.co/SdNvjytDpi

你只要刷一圈，就会发现：真正好用的 Skill，都不是"堆功能"，而是把一个具体场景打磨到极致。

官方 Skills

如果只挑一个仓库去精读，那一定是 Anthropic 官方的：
https://t.co/Tc0WvAPwcf

它不是那种"随便丢几个 demo 应付下社区"的项目，而是把 Claude 线上真正在跑的生产级能力，原封不动摊开给你看：
文档处理四大件：Word / PDF / PPT / Excel，从创建、编辑到分析，流程写得极细，提示词、参数、边界都清清楚楚。

开发者工具：MCP 服务器、Web 应用测试、Artifacts 构建，一看就是为真实工程环境设计的。

创意设计：算法艺术、Canvas 设计、主题工厂，不是玩票，是能直接拿去跑活的方案。

更关键的是，你在 https://t.co/3aAaYssIbc 里点的那些"文档创建""智能分析"，背后就是这些 Skill。

也就是说，这个库本质是"官方拆解自家产品的内部能力模型"。

安装也很简单，要么从官方插件市场点一点，要么直接用命令挂上去：

/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills

## 2
https://x.com/xiaoerzhan/status/2007603079122923803

原文链接在这里，更多信息：https://t.co/v4UuvNkZl2…
---

---
url: "https://x.com/iamtonyzhu/status/2006243191893418345"
requested_url: "https://x.com/i/status/2006243191893418345"
author: "Tony出海 (@iamtonyzhu)"
author_name: "Tony出海"
author_username: "iamtonyzhu"
author_url: "https://x.com/iamtonyzhu"
tweet_count: 9
---

## 1
https://x.com/iamtonyzhu/status/2006243191893418345

orange 老师写了 Claude code 入门指南拿了 100 万流量，
我写一篇长文 Claude Agent Skills 入门指南🎉，欢迎收藏

Anthropic这家公司可以说是一直是引领 AI 方向。

2023 年，OpenAI 听说Anthropic要推出一个 AI 聊天 bot，抢先发布了类似的 bot 就是 ChatGPT，占据先手。 

Claude code 作为第一次最成功的  Agent，掀起来了 2025 年的 Agent 元年。

Anthropic推出的 MCP 大模型数据交换框架，成为 OpenAI 等跟随的行业标准。

Anthropic推出的 Agent skills 将成为 2026 年最重要的行业原因，更多的普通人能够通过创建和挑选适合自己的大模型技能，能够更好的完成工作。比起 n8n 那种复杂的工作流，skills 是学习成本最低的。

前两天都被 Manus 刷屏了，我用一个新类似的 AI 产品 https://t.co/OkJbXCqn4R 来整理和协助思路写了这篇《Claude Agent Skills 入门指南》👇

![](https://pbs.twimg.com/media/G9ebi5oaYAEyQqX.jpg)

## 2
https://x.com/iamtonyzhu/status/2006243198180733327

为什么 agent skills 是跳不过去的？

 发展了 3 年的聊天 AI，缺乏执行特定、复杂工作流程的“专才”能力。对我们追求的是能理解、规划并高效执行任务的 AI 智能体（Agent）。

Agent Skills 便是解决这一核心痛点的关键技术。它是一种开放标准，旨在将专业知识和工作流程打包成 AI 可理解、可复用的“技能包”，让 AI 从“通才”转变为“专家”。

本教程将带你深入了解 Agent Skills 的核心概念、与相关技术的区别，并通过一个实战案例，教你如何从零开始构建一个自己的 Skill。

1. 核心问题：AI Agent 为何需要“技能”？

通用大模型在执行专业任务时面临三大挑战：

a， 上下文窗口限制： 无法将海量的专业知识（如公司内部的开发规范、品牌设计指南）一次性灌输给模型。

b， 流程不确定性： 即使通过提示词进行指导，AI 在执行多步骤、复杂任务时，其输出结果和行为也常常不稳定、不一致。

c， 高昂的 Token 成本： 每次请求都附带大量重复的背景信息和指令，导致成本高昂且效率低下。

Agent Skills 通过“程序化知识封装”解决了这些问题。 它不是简单的提示词，而更像是一份标准作业程序（SOP）或一本给 AI 的“岗前培训手册”。

2. 什么是 Agent Skills？

根据官方规范，一个 Agent Skill 本质上是一个结构化的文件夹。

其最简结构仅包含一个核心文件：SKILL .md。

your-skill-name/
└── SKILL .md

这个 SKILL .md 文件通过 YAML frontmatter 定义元数据，通过 Markdown 正文提供详细指令。

•元数据 (Metadata): 告诉 Agent 这个 Skill 的“身份”和“用途”。
◦name: 技能的唯一标识，必须与文件夹名一致。
◦description: 功能描述，是 Agent 决定是否激活此技能的关键依据。

•指令 (Instructions): 告诉 Agent 在激活此技能后，应该“如何做”。这是分步的工作流指南。
关键机制：渐进式信息披露 (Progressive Disclosure)

Agent Skills 的设计精髓在于其高效的 Token 利用机制，它分三层按需加载信息：

第一层：元数据 (Metadata)Agent 启动时，仅加载所有可用 Skills 的 name 和 description。这消耗的 Token 极少，但足以让 Agent 对其能力库有一个全局认知。

第二层：核心指令 (Core Instructions)当用户的请求与某个 Skill 的 description 匹配时，Agent 才会完整加载该 Skill 的 SKILL .md 文件内容，获取详细的操作指南。

第三层：支持资源 (Supporting Resources)如果 SKILL .md 的指令中引用了外部脚本（位于 scripts/ 目录）或参考文档（位于 references/ 目录），Agent 仅在执行到该步骤时才会去访问这些文件。特别地，当执行脚本时，只有脚本的输出结果会进入上下文，代码本身不会，极大地节省了成本并保证了执行的确定性。

这种分层机制确保了 Agent 在具备强大扩展性的同时，运行成本极低且响应迅速。

Anthropic 在 GitHub 上开源了一系列的 Agent Skills：
https://t.co/33Oul5ds8C

推荐 agent skills 资源列表

https://t.co/1DJMOo1zEQ

2， 安装和使用 Agent Skills

步骤一：下载

Agent Skills 和 MCP 一样都是 anthropics 公司提出来的，所以他们也提供了很多好用的 skills 供大家使用，如果选择将官方 Skills 安装到当前项目，就在终端输入这条命令：

openskills install anthropics/skills

安装成功后，你就会在Cursor、Trae等工具的文件管理区看到 .claude/skills 的文件夹。

当然也可去下面三方的收集网站上面下载别人写好的 skills：
https://t.co/uQLMRKrfKU
https://t.co/o5Qpejlggu

步骤二：配置
先在项目根目录创建一个 https://t.co/YZ81JqufVb 文件，然后运行

openskills sync

确认后按回车键，你选择的 Skills 就会写进之前空白的 https://t.co/YZ81JqufVb 文档中。

它将作为 Cursor、Trae 等 Coding Agent 接下来使用 Skills 的指导文件。

步骤三，调用
Skills 是可以被自动调用的，如果你想手动调用，可以直接在提示词中指定要调用的具体 Skills

未完👇

## 3
https://x.com/iamtonyzhu/status/2006243204304363779

3，实例做一个公众号润色 skills

1）进入目录，创建skill的文件件
  进入AnythingLLM的安装目录，
  进入子文件夹storage\plugins\agent-skills，在这下边创建你skill文件夹（文件夹名称要和后边的配置对上），

创建的文件夹叫 weixin
-document-expert

2）创建https://t.co/DBcLe6TEjp
   说明：这个是skill标准文件，注意名字大写。

内容如下：
Plain   Text
---
   name: weixin-document-expert
   description: 当用户需要写公众号文章时，请调用此技能进行专业润色。
   ---
   # 技能指令
name: weixin-public-account-polisher
description: 当用户需要写/改公众号文章时，提供“情绪优先”的专业润色与结构优化：在不改变核心原意的前提下，让文章更好读、更有共鸣、更容易被转发与推荐。

技能指令

当用户输入一段文字并要求“润色 / 改成公众号风格 / 提升阅读与转发”时，遵循以下 SOP（公众号第一性原理：情绪驱动传播）：

SOP

1.情绪锚点提炼（必做）
•识别这段内容最核心的读者情绪：焦虑/愤怒/委屈/希望/爽感/安全感/优越感等。
•明确目标人群与“痛点一句话”，并把它放到标题或开头三句话里。

2.口语到“公众号可读表达”转换
•不走公文腔；保留作者个性，但把松散口语改成更有质感、更利落的书面表达。
•例：
•“我打算做”→“我准备把这件事做成” / “我决定开始做”
•“其实就是”→“本质上是”
•“很重要”→“决定成败的关键在于”

3.句式精简与节奏优化
•删除冗余修饰、重复解释、绕圈铺垫；多用短句、对比句、排比句增强节奏。
•关键观点前后加“停顿感”（换行/分段），提高手机端阅读舒适度。

4.结构重排（长文必做）
•将散点观点改为层级结构：
•“一句结论开头”→“一是/二是/三是”→“总结+行动建议/金句收口”。
•优先使用：结论先行、先痛点后方法、先共鸣后干货。

5.转发触发器植入（可选但强烈建议）
围绕三类转发欲，补强表达而不新增硬编事实：
•有用：教人一招，节省时间/金钱/试错
•有趣：让人放松、爽、好读
•共鸣：把“读者心声”说出来，让人觉得“你懂我”

6.公众号内容策略对齐（写作原则内置）
•公众号属于“内容交付”，流量需要从外部找入口再承接。
•铁粉才是粉：垂直很重要；如果推出去只有少数人感兴趣，会影响后续推荐。
•一个内容一个号往往是更优的流量选择。
•日更/高频保持存在感：让读者知道你还在。
•稳定小爆款比随机大爆款更有长期价值与变现能力。
•半原创更吃香：在“大家都知道的领域”做介绍与解读，建立链接；纯原创往往难形成共识与传播。

⸻

输出格式（默认）
•润色后的公众号正文（可直接发布）
•标题备选 3–5 个（偏情绪/偏利益/偏共鸣各至少 1 个）
•修改要点清单（只说明怎么改，不改变你的核心意思）
•（可选）结尾引导一句（关注/点赞/转发/留言的自然引导，不硬要）

⸻

禁止行为
•不改变用户核心原意与立场；不擅自添加虚构经历/数据/案例。
•严禁出现表情包、过于轻快油滑的语气。
•不写“自嗨式原创炫技”，以读者感受与传播为准。

## 4
https://x.com/iamtonyzhu/status/2006287286842061217

为什么要学  Claude skills ？
万能 Claude skills 可能要重新定义软件行业了

写一个skill调用Calibre实现任意格式互相转换，几分钟后就开发好了。实现电子书格式转换自由了！

https://t.co/uNDUdQtsef

> Author: 向阳乔木 (@vista8)
> URL: https://x.com/vista8/status/2004352512535703752
>
> 实现电子书格式转换自由了！太爽了~
>
> 只需安装经典免费软件 Calibre。
>
> 跟Claude Code说，写一个skill调用Calibre实现任意格式互相转换，几分钟后就开发好了。
>
> 比如epub转pdf、Markdown转epub，Mobi转epub都可以。
>
> 不用自己开软件操作，能跟其他Skill配合用。
>
> NotebookLM Skill不支持epub，转成pdf上传
>
> Calibre下载地址见评论区

## 5
https://x.com/iamtonyzhu/status/2006287720814125061

学 skills 比想象的简单 100 倍，根本不像 n8n 那样复杂。

https://t.co/xsxFJymaxU

> Author: 向阳乔木 (@vista8)
> URL: https://x.com/vista8/status/2004226986353611086
>
> 扔文本就能用！Claude Skills比你想的简单100倍！
>
> Claude Skills 就是 Markdown 加一点点 YAML 元数据。
>
> 再加一些可选的资源、参考文档和可执行脚本。
>
> 更接近 LLM 精神：扔进去一些文本，让模型自己搞定。
>
> 且不局限于Claude。
>
>  Codex CLI 或 Gemini CLI 也能读取使用。
>
> 比如安装一个pdf skill，要求 "读取 pdf/SKILL.md 然后给我创建一个描述项目的 PDF"，一样能搞定。
>
> 尽管这些工具和模型根本不知道 skills 系统存在。
>
> 简单是硬道理。
>
> 原文地址见评论

## 6
https://x.com/iamtonyzhu/status/2006318016582357396

Claude skills 应用场景都有哪些应用场景与技能分类？

📄 文档处理
Word文档批量编辑、格式审查与批注
PDF文字、表格、元数据提取与合并标注
PPT幻灯片生成与模板优化
Excel公式处理与数据可视化
Markdown转EPUB电子书转换器

💻 开发与编码辅助
React/Tailwind前端组件构建
AWS架构部署优化
Git提交历史生成用户版本变更记录
iOS模拟器交互调试
D3数据可视化图表生成
Playwright自动化测试
Claude Code终端窗口动态标题命名
子代理并发开发 + 代码审查
Move语言代码质量分析

📊 数据与分析
CSV文件可视化摘要报告
PostgreSQL 安全只读查询
错误追踪回溯分析

📈 商业与营销
品牌规范自动应用
竞品广告分析器
域名创意生成 + TLD可用性检查
内部通讯自动撰写助手
高质量客户线索识别与推荐

✍️ 沟通与写作
网页文章内容提取
点子头脑风暴扩展
AI写作辅助 + 内容结构反馈
家族史研究辅助
会议记录行为模式分析
NotebookLM集成：基于文档溯源回答

🎨 创意与媒体
视觉设计输出PNG/PDF
图像增强器：高清重制演示图
Slack动画GIF生成器
幻灯片/文档主题风格模板库
YouTube视频下载与转录总结
Gemini图像生成API调用支持

📁 效率与组织
智能文件/发票分类与重命名
Kaizen持续改进分析法
n8n工作流自动理解与执行
抽奖工具、文档网络化整理

🤝 协作与项目管理
Git推送自动化
实现计划与测试修复的自动评审
错误修复与测试调整建议

🔐 安全与系统
数字取证与文件元数据提取
安全文件删除、Sigma规则威胁检测

推荐这个工具免费使用 https://t.co/CvDLoNtq40

![](https://pbs.twimg.com/media/G9ffC9ra4AAqxDX.jpg)

## 7
https://x.com/iamtonyzhu/status/2006320043903287705

15分 Claude skills  非技术人员指南🔥👇

如果你没有使用 claude skills，你就错过了。

它们看起来可能有点吓人，但实际上设置起来超级简单。以下是方法（下面的链接中有图片）：

1/ 确保在设置 > 功能 > 技能中启用了 claude skills

2/ 在设置中的技能下开启“skill-creator”技能。这是元技能，你可以用它让 claude 为你构建其他技能

3/ 打开一个新的聊天窗口，让 claude 使用“skill-creator”技能帮助你创建一个新技能

4/ 详细描述你想创建的技能，具体说明你需要的输出（你也可以让一个现有项目通过请求该项目使用“skill-creator”将其转化为技能）

5/ claude 可能会问一些澄清问题，然后构建出完整的技能文件和一个 read-me 文档

6/ 阅读 read-me 文档并下载它创建的技能文件。这会告诉你它创建了什么，以及让你运行它的下一步步骤

7/ 返回设置 > 功能 > 技能 > 上传技能。选择你下载的文件并上传它。它会将其添加到你的技能列表中。确保切换开关打开，这样你就知道它已激活

8/ 在一个新聊天中测试它，通过让 claude 使用你的技能名称来调用它

9/ 如果你的技能没有创建你需要的输出，返回你创建该技能的对话中，告诉它你想更改什么（如果你进行编辑，你需要在设置中上传技能文件的新版本，并关闭旧版本）

从一些简单的东西开始（你已经经常做的事情）。你会在过程中逐步搞定其余部分。

## 8
https://x.com/iamtonyzhu/status/2006321279641727337

Claude Pro  账号价值太大了，还没有订阅，或者经常被封号困扰，支付卡困扰的推荐这个代充网站靠谱 👇https://t.co/uu1sBBtzbs

## 9
https://x.com/iamtonyzhu/status/2006692040831373714

最近 Claude skills 的资料非常多，到搜集导入 https://t.co/QZIJS5SUUz 整理和创作一把梭。 https://t.co/rrTBqhWRwQ

![video](https://pbs.twimg.com/amplify_video_thumb/2006691751843737604/img/5HOs4UlKLnr75zQb.jpg)
[video](https://video.twimg.com/amplify_video/2006691751843737604/vid/avc1/1152x720/4gp-SCh1yM3KlgxB.mp4?tag=21)
---

---
url: "https://x.com/xiaohua_888/status/2006198122402193531"
requested_url: "https://x.com/i/status/2006198122402193531"
author: "1024 (@xiaohua_888)"
author_name: "1024"
author_username: "xiaohua_888"
author_url: "https://x.com/xiaohua_888"
tweet_count: 1
---

## 1
https://x.com/xiaohua_888/status/2006198122402193531

很多人用AI写代码，能跑，但一个月后各种 bug 冒出来，改一个出三个

问题出在哪？AI 默认只会写"看起来合理"的代码，不是"专业级"的代码

解决方案：给 AI 装上 Skill

分享三个我觉得最值得用的 Skill：

Frontend Design（前端设计）
Anthropic 官方出的，让你的界面从"能看"变成"想用"，不懂设计也能搞出科技感满满的 UI

API Design Principles（API 设计）
接口命名、错误码、分页、认证……这些老程序员才能积累的东西，一个 Skill 搞定

Postgres Table Design（数据库设计）
帮你绕过那些"几个月后才会爆发"的坑，不用等系统崩了才知道表设计有问题

Skill 的本质，就是把"专家经验"变成"可复用的知识包"

获取skill👇
https://t.co/u0QyjXMX7Z
---

---
url: "https://x.com/iamzhihui/status/2005558493735244077"
requested_url: "https://x.com/i/status/2005558493735244077"
author: "志辉 (@iamzhihui)"
author_name: "志辉"
author_username: "iamzhihui"
author_url: "https://x.com/iamzhihui"
tweet_count: 2
---

## 1
https://x.com/iamzhihui/status/2005558493735244077

终于肝完这个 Claude skills
给我节省了百万上下文的 token
爽翻 Vibe Coding

那就是 browser skills

为什么要做这个呢？

大家对 Playwright、Chrome DevTools 这些 MCP 应该不陌生，但这些 MCP 对上下文的占用是非常大的。

❗记住：这些占用是进入 Claude Code 就开始的，而不是你使用它们的时候。

尤其是浏览器这些 MCP 有很多工具，至少都有 10 多到 20 多种以上。图片中，我只安装了 Chrome DevTools，就占用了 8.8% 的上下文，关键是我还什么都没做。

所以，开发或者寻找一个浏览器的技能是很有必要的，因为技能不会一开始就占用那么多的上下文。

✅ 好消息是 Mario Zechner 做了一个案例，Factory 大善人帮我们整理成文章，最后我把它做到了我的仓库里。

✅ 安装方法其实也很简单：
/plugin marketplace add iamzhihuix/happy-claude-skills
/plugin install browser@happy-claude-skills

使用提示词：可以使用浏览器技能进行测试。

> Author: 志辉 (@iamzhihui)
> URL: https://x.com/iamzhihui/status/2004854569462100176
>
> 最近 Claude Skills 越来越火，大家都在聊怎么用它提升效率。
>
> 我自己用 Claude Code 很久了，之前最烦的就是面对一大堆 Skills，不知道哪个靠谱、哪个真正能解决问题。
>
> 到处试来试去，不是效果一般就是安装麻烦，浪费时间。
>
> 所以我把日常高频用、反复验证过的几个 Skills 整理了一下，全部开源给大家！
>
> 项目上线：happy-claude-skills
>
> 只放真正“好用”的，不多，就几个精品，避免大家选择困难。
> 目前包含这些实用 Skills：
>
> ✅ docx-format-replicator
> 完美复制 Word 文档样式。
> 上传模板，它自动提取格式，生成一样的新文档。
> 报告、简历、合同批量处理，省时省力！
>
> ✅ video-processor
> 直接输入 YouTube 链接，就能转录、总结视频内容。
> 不用再找其他工具或付费服务，在 Claude Code 里一键搞定视频笔记或摘要。
>
> ✅ wechat-article-writer
> 公众号写作助手。
> 内置快速写作流程：研究话题、生成大纲、正文、标题优化、排版建议。
> 帮你更快写出阅读量更高的文章。
>
> 这些都是我自己日常用着顺手的，简单可靠。
> 安装很简单，在 Claude Code 里输入：
>
> /plugin marketplace add iamzhihuix/happy-claude-skills
>
> 下一步就是你想要哪个 plugin
> /plugin install docx-format-replicator@happy-claude-skills
> /plugin install video-processor@happy-claude-skills
> /plugin install wechat-article-writer@happy-claude-skills
>
> 项目地址（欢迎 star 支持一下～）：
> https://t.co/yrpfzzyOjJ
>
> 试过之后，Claude 就从聊天工具变成了真·生产力助手。
> 如果你也想少折腾、多干活，推荐试试这个小合集。
>
> 评论区聊聊你的使用感受，或者有什么想加的 Skills，一起迭代！

![](https://pbs.twimg.com/media/G9Us0TtboAAPmKn.jpg)
![](https://pbs.twimg.com/media/G9Us0jIbUAA2loV.jpg)

## 2
https://x.com/iamzhihui/status/2005558506347446461

感谢 factory 大善人总结的 skills
https://t.co/JZPFmSvSl4
---

---
url: "https://x.com/vista8/status/2005105050348388512"
requested_url: "https://x.com/i/status/2005105050348388512"
author: "向阳乔木 (@vista8)"
author_name: "向阳乔木"
author_username: "vista8"
author_url: "https://x.com/vista8"
tweet_count: 2
---

## 1
https://x.com/vista8/status/2005105050348388512

经常读完公众号文章，不知道怎么写推荐语分享。

且公众号防爬严重，找到一个专门用于读公众号文章内容的MCP，原理是用Playwright模拟访问获取。

打包到Claude Skill，读取文章，写转发推荐语。

MCP地址见评论区

![](https://pbs.twimg.com/media/G9OPwa2XcAAfV6K.jpg)

## 2
https://x.com/vista8/status/2005105150726455369

微信文章内容读取MCP ：https://t.co/EyIZpjgeFb
---

---
url: "https://x.com/DailyDoseOfDS_/status/2005209632177053988"
requested_url: "https://x.com/i/status/2005209632177053988"
author: "Daily Dose of Data Science (@DailyDoseOfDS_)"
author_name: "Daily Dose of Data Science"
author_username: "DailyDoseOfDS_"
author_url: "https://x.com/DailyDoseOfDS_"
tweet_count: 1
---

## 1
https://x.com/DailyDoseOfDS_/status/2005209632177053988

Claude Scientific Skills.

Turn Claude into your AI research assistant capable of executing complex multi-step scientific workflows across maths, biology, chemistry, medicine, and beyond.

100% open-source (123+ skills). https://t.co/P5tSrta6y0

![](https://pbs.twimg.com/media/G9PviJTacAAYZe-.jpg)
---

---
url: "https://x.com/vista8/status/2004956277353680926"
requested_url: "https://x.com/i/status/2004956277353680926"
author: "向阳乔木 (@vista8)"
author_name: "向阳乔木"
author_username: "vista8"
author_url: "https://x.com/vista8"
tweet_count: 1
---

## 1
https://x.com/vista8/status/2004956277353680926

把这个库做成了skill，在Claude Code支持下。

实现用自然语言处理处理视频。

比如给视频加上配乐，自动截图、调整倍速等。 https://t.co/57KWceVJDa

> Author: 向阳乔木 (@vista8)
> URL: https://x.com/vista8/status/2004948184565776386
>
> 一句话安装这个工具，用命令行处理视频，不用记复杂的ffmpeg命令。
>
> 安装：npm install -g ezff
>
> 安装后，在终端输入 ff 启动，粘贴视频地址回车。
>
> 选择对应操作，比如转换视频格式、压缩、改分辨率、调整倍速等。
>
> 支持简单自然语言处理视频，比如
>
> ff convert video.mp4 to gif
> ff convert video.mp4 to mp3
>
> 压缩到10Mb
> ff compress video.mp4 to 10mb
>
> 裁切指定时间段
> ff trim video.mp4 from 0:30 to 1:00
>
> 提取音频
> ff extract audio from video.mp4
>
> 调整速度
> ff speed up video.mp4 by 2x
> ff slow down video.mp4 by 2x

![](https://pbs.twimg.com/media/G9MIuQUbQAAZGPR.jpg)
---

---
url: "https://x.com/PMbackttfuture/status/2004205626004828169"
requested_url: "https://x.com/i/status/2004205626004828169"
author: "AI产品黄叔 (@PMbackttfuture)"
author_name: "AI产品黄叔"
author_username: "PMbackttfuture"
author_url: "https://x.com/PMbackttfuture"
tweet_count: 1
---

## 1
https://x.com/PMbackttfuture/status/2004205626004828169

想更新一些用Skills实现的SOP

第一个是微信群聊自动总结并发布到网站

主要通过Chatlog读取、指定格式整理、自动同步Github完成

里面还有第二个Skills
根据指定的群聊
自动读取、提取洞察、整理成HTML

后面还会更新更多实操Case
大家对Skills有什么希望实现的也可以留言！ https://t.co/NueolGW1Dj

![video](https://pbs.twimg.com/amplify_video_thumb/2004198242406543360/img/zIiy2swUN4CL1fBf.jpg)
[video](https://video.twimg.com/amplify_video/2004198242406543360/vid/avc1/3680x2160/nHrFkD6oXYVT6A-p.mp4?tag=21)
---

---
url: "https://x.com/vista8/status/2004229308844290401"
requested_url: "https://x.com/i/status/2004229308844290401"
author: "向阳乔木 (@vista8)"
author_name: "向阳乔木"
author_username: "vista8"
author_url: "https://x.com/vista8"
tweet_count: 3
---

## 1
https://x.com/vista8/status/2004229308844290401

发现了个牛逼的skill，竟然能NotebookLM打通！

这样上传Pdf、Youtube字幕，自动提问获取答案，再创作，自动化学习东西就更强了。

等我先测试下，地址见评论

![](https://pbs.twimg.com/media/G9Bz5bxakAE0Jqu.jpg)

## 2
https://x.com/vista8/status/2004229427744616685

NotebookLM Claude skill：https://t.co/p72AgWfHFC

## 3
https://x.com/vista8/status/2004232285932195951

我去，竟然真的可以，这下用处大了。 https://t.co/gePbvx8cbn

![](https://pbs.twimg.com/media/G9B2ogfaUAA1Qlv.jpg)
---

---
url: "https://x.com/vista8/status/2003658462182637763"
requested_url: "https://x.com/i/status/2003658462182637763"
author: "向阳乔木 (@vista8)"
author_name: "向阳乔木"
author_username: "vista8"
author_url: "https://x.com/vista8"
tweet_count: 1
---

## 1
https://x.com/vista8/status/2003658462182637763

正在写一个Skill，每天自动获取最新的AI资讯和论文。

给出翻译和写作选题。 https://t.co/Y7P6P4f8ZK

> Author: 向阳乔木 (@vista8)
> URL: https://x.com/vista8/status/2003288079340392839
>
> 朋友们，你们用claude skills做了什么有点酷的东西，求分享。
>
> 曾听过，一个年轻geek朋友，连接安卓手机，用Claude Skills 每天刷200个低粉高赞美女抖音，点赞留言找对象...
>
> 据他说，跟真人浏览差不多，还不会被封...

![](https://pbs.twimg.com/media/G85sqQ2a0AAzJed.jpg)
---

---
url: "https://x.com/tuzi_ai/status/2003442051002888661"
requested_url: "https://x.com/i/status/2003442051002888661"
author: "兔妹_兔子 (@tuzi_ai)"
author_name: "兔妹_兔子"
author_username: "tuzi_ai"
author_url: "https://x.com/tuzi_ai"
tweet_count: 1
---

## 1
https://x.com/tuzi_ai/status/2003442051002888661

用Claudecode 数月都没尝试过 skills，今天看乔木老师的体验，也来了动力去检索一些相关视频。

看完“一个视频让你彻底掌握Claude Code Skills”后，感觉这挺像GPTS 的，预设一些常用的输入和要求，减少交互时间（像 ChatGPT 对话中需要这个预设角色的话可以@它）

视频地址：https://t.co/896mkjOqXA https://t.co/7SJT6JfhfQ

> Author: 向阳乔木 (@vista8)
> URL: https://x.com/vista8/status/2003410985743442171
>
> 感觉 Skills .md 是一套执行手册 + 脚本 + MCP + API调用的工具打包，更像操作手册SOP。
>
> 适合做更灵活的 Workflow 解决特定场景问题，可理解为个人版的Agent搭建工具？
>
> CLAUDE .md 更像为Claude Code服务的系统提示词、工具调用规则等。
>
> Skill 有点像克隆一个小号垂直的Claude Code。
>
> ---
> 不知道这个理解对不对

![video](https://pbs.twimg.com/amplify_video_thumb/2003441110496976896/img/EoZyBFLsJSEdet2Z.jpg)
[video](https://video.twimg.com/amplify_video/2003441110496976896/vid/avc1/1734x1080/R4RMu2lFsF9x7AVq.mp4?tag=21)
---

---
url: "https://x.com/DataChaz/status/2003378266061832348"
requested_url: "https://x.com/i/status/2003378266061832348"
author: "Charly Wargnier (@DataChaz)"
author_name: "Charly Wargnier"
author_username: "DataChaz"
author_url: "https://x.com/DataChaz"
tweet_count: 3
---

## 1
https://x.com/DataChaz/status/2003378266061832348

Wild.

By far the most complete Claude Skills repo yet 🤯

@Composio’s Awesome-Claude-Skills packs 100`s of ready-to-use workflows:
↳ PDF tools, changelog generation
↳ Playwright automation
↳ AWS/CDK tools, MCP builders

... and much more!

Free and open-source.

Repo in 🧵↓ https://t.co/kJhZHLU5OA

![](https://pbs.twimg.com/media/G81t6rIaEAA6T5t.jpg)

## 2
https://x.com/DataChaz/status/2003378278074319350

https://t.co/ztFXuelwXD

## 3
https://x.com/DataChaz/status/2003837659278667862

there goes my Xmas break 😅
---

---
url: "https://x.com/cloudxdev/status/2003097964865102224"
requested_url: "https://x.com/i/status/2003097964865102224"
author: "CloudAI-X (@cloudxdev)"
author_name: "CloudAI-X"
author_username: "cloudxdev"
author_url: "https://x.com/cloudxdev"
tweet_count: 1
---

## 1
https://x.com/cloudxdev/status/2003097964865102224

SKILL[.]md that could be helpful, bookmark it 📁

-----

## name: creating-landing-pages
description: Creates distinctive, award-winning landing pages as single-file HTML with embedded CSS/JS. Generates production-ready marketing pages, startup websites, product launch pages, and conversion funnels with bold typography, orchestrated animations, and memorable aesthetics. Avoids generic AI patterns. Use when asked to build a landing page, marketing site, product page, startup website, or conversion-focused webpage.

# Creating Landing Pages

Generates distinctive landing pages that avoid generic AI aesthetics. Output is a single HTML file with embedded CSS and JavaScript.

## Before Coding

Gather from user (or infer from context):

- Company/product name and one-line description
- Target audience
- Primary CTA (e.g., “Start Free Trial”)
- Secondary CTA (e.g., “Watch Demo”)

## Aesthetic Direction

Commit fully to ONE direction:

|Direction      |When to Use                                             |
|---------------|--------------------------------------------------------|
|Ink & Paper    |B2B, content, publishing — serif drama, high contrast   |
|Neon Terminal  |Dev tools, tech — CRT glow, monospace, dark theme       |
|Brutalist Mono |Creative agencies — raw textures, exposed structure     |
|Soft Luxury    |Premium products — warm neutrals, refined serifs        |
|Retro-Future   |Consumer apps — Y2K gradients, metallics                |
|Swiss Precision|Enterprise, fintech — rigid grids, functional sans      |
|Organic Flow   |Wellness, sustainability — nature palettes, fluid shapes|

Choose the most unexpected yet appropriate option.

## Required Sections

1. **Hero**: Intriguing hook, interactive element, ≤12-word value prop, primary CTA, trust signals
2. **Problem/Solution**: Story-driven narrative with scroll-triggered reveals
3. **Product Showcase**: Animated mockup or interactive demo preview
4. **Social Proof**: Testimonials, metrics, customer grid with hover states
5. **Technical Differentiators**: Feature comparison, integrations, security badges
6. **Conversion**: Secondary CTA, minimal form (Name, Email, Company)
7. **Footer**: Minimal links, newsletter capture

## Anti-Patterns

Never use:

- Purple/blue gradients on white backgrounds
- Inter, Roboto, Arial, Open Sans, system-ui fonts
- Generic hero-CTA-features-testimonials template flow
- Abstract blobs or generic geometric shapes
- #6366F1 or similar overused accent colors
- 16px border-radius on everything
- Drop shadows on all cards
- Lorem ipsum placeholder text

## Technical Output

Single HTML file containing:

- CSS in `<style>` tag with CSS custom properties
- JavaScript in `<script>` tag (Intersection Observer for scroll reveals)
- Google Fonts via `<link>`
- Mobile-responsive with fluid typography
- Orchestrated page-load animations (staggered with animation-delay)
- Hover micro-interactions

## Design Tokens Template

```css
:root {
  --font-display: 'Playfair Display', serif;
  --font-body: 'Source Serif Pro', serif;
  --color-bg: #0a0a0f;
  --color-text: #ffffff;
  --color-muted: #a0a0a0;
  --color-accent: #00ff88;
  --ease-out-expo: cubic-bezier(0.19, 1, 0.22, 1);
}
```

## Pre-Code Checklist

Before writing code, decide:

1. Aesthetic direction
2. Font pairing (display + body)
3. Color palette (max 5 hex values)
4. Hero hook concept
5. One unique interactive element

Generate realistic placeholder content appropriate to the company context.
---

---
url: "https://x.com/vista8/status/2003069573679997258"
requested_url: "https://x.com/i/status/2003069573679997258"
author: "向阳乔木 (@vista8)"
author_name: "向阳乔木"
author_username: "vista8"
author_url: "https://x.com/vista8"
tweet_count: 1
---

## 1
https://x.com/vista8/status/2003069573679997258

AI做了个 "论文翻译器"：自动写文＋配图＋发布。

写了一个Claude skills，提供论文URL，按指定提示词生成 Markdown 文章。

第二遍会反思推理，润色文章，自动截图论文图表配图、调Nano Banana Pro生图。

配合Obsidian插件NoteToMP，一键发布到公众号草稿。

![](https://pbs.twimg.com/media/G8xUVWebgAAKZGd.jpg)
---

---
url: "https://x.com/shao__meng/status/2002909709742092524"
requested_url: "https://x.com/i/status/2002909709742092524"
author: "meng shao (@shao__meng)"
author_name: "meng shao"
author_username: "shao__meng"
author_url: "https://x.com/shao__meng"
tweet_count: 1
---

## 1
https://x.com/shao__meng/status/2002909709742092524

[开源推荐] Skills: Anthropic 官方 Agent Skills 精选资源和最佳实践库

Anthropic 官方开源的这个项目展示了从创意到企业级的完整谱系，证明 Skills 系统能处理高度专业化的重复任务。目前仓库中共包含 16 个技能，分为几大类别 🔽

1. 文档处理类（最复杂、生产级）
· docx：处理 Microsoft Word 文档生成/编辑
· pdf：PDF 文件操作（如表单字段提取、图像处理）
· pptx：PowerPoint 幻灯片生成/编辑
· xlsx：Excel 表格处理
· doc-coauthoring：文档协同编辑

2. 创意与设计类
· algorithmic-art：算法生成艺术
· canvas-design：画布式视觉设计（如海报、艺术品）
· frontend-design：前端界面高品质设计（最近更新）
· theme-factory：主题生成
· brand-guidelines：品牌指南应用

3. 开发与技术类
· webapp-testing：Web 应用自动化测试（复杂度高）
· web-artifacts-builder：Web 组件构建
· mcp-builder：模块化组件构建

4. 企业与沟通类
· internal-comms：内部沟通工作流
· slack-gif-creator：Slack GIF 生成

5. 元技能
· skill-creator：帮助创建新技能的“技能生成器”，极大降低自定义门槛，是扩展性的关键体现

开源地址
https://t.co/I9PkD8H203

![](https://pbs.twimg.com/media/G8vDuJiWYAASxRx.jpg)
---

---
url: "https://x.com/dotey/status/2000295963420660144"
requested_url: "https://x.com/i/status/2000295963420660144"
author: "宝玉 (@dotey)"
author_name: "宝玉"
author_username: "dotey"
author_url: "https://x.com/dotey"
tweet_count: 2
---

## 1
https://x.com/dotey/status/2000295963420660144

OpenAI 也已经悄悄支持了竞争对手 Anthropic 提出的“Skill”机制，在 Codex CLI 已经支持，并且在 ChatGPT 的代码解释器 (Code Interpreter) 中也悄悄使用了。

Skill 很简单强大，只需要就是一个文件夹，里面放个 Markdown 格式的说明文档，再加上一点可选的资源或脚本。理论上，任何能够浏览和读取文件系统的 LLM 工具，应该都能使用它。

ChatGPT 目前添加的技能包括：电子表格、Word 文档 (docx) 和 PDF的处理。

其中对于 PDF 和文档处理，他们的策略是先把每一页转换成图片的 PNG 格式，然后传给具备视觉能力的 GPT 模型。这大概是为了保留排版和图表信息，如果直接提取纯文本，这些信息往往会丢失。

在 ChatGPT 中，说一句
> Create a zip file of /home/oai/skills
(把 /home/oai/skills 打包成 zip 文件)
有一定概率提供文件打包

> Author: Simon Willison (@simonw)
> URL: https://x.com/simonw/status/1999623295046664294
>
> OpenAI aren't talking about it yet, but it turns out they've adopted Anthropic's brilliant "skills" mechanism in a big way
>
> Skills are now live in both ChatGPT and their Codex CLI tool, I wrote up some detailed notes on how they work so far here: https://t.co/eWcaA3PTKp

![](https://pbs.twimg.com/media/G8J4zCAWoAM3YSM.jpg)
![](https://pbs.twimg.com/media/G8J6SyYXkAYtooR.jpg)

## 2
https://x.com/dotey/status/2000296362378932450

或者你可以到这个repo看：https://t.co/wb5kt9RFmZ
---

---
url: "https://x.com/bourneliu66/status/2000208636094627995"
requested_url: "https://x.com/i/status/2000208636094627995"
author: "刘小排 (@bourneliu66)"
author_name: "刘小排"
author_username: "bourneliu66"
author_url: "https://x.com/bourneliu66"
tweet_count: 1
---

## 1
https://x.com/bourneliu66/status/2000208636094627995

我们对 AI 的终极想象，往往是一个无所不能的超级管家，一个只需一声令下就能搞定一切的通用智能体（Agent）。

但最近， Anthropic 的两位技术专家 Barry Zhang 和 Mahesh Murag给了业界一个醍醐灌顶的建议：

“别再构建庞大的Agent了，去构建一个个精巧的Skill吧。”
https://t.co/NNIsJjp6gy

![](https://pbs.twimg.com/media/G8Iq4MuWUAMNZdq.jpg)
![](https://pbs.twimg.com/media/G8Iq6AjXsAEYCx6.jpg)
---

---
url: "https://x.com/nummanali/status/2000194213359562907"
requested_url: "https://x.com/i/status/2000194213359562907"
author: "Numman Ali (@nummanali)"
author_name: "Numman Ali"
author_username: "nummanali"
author_url: "https://x.com/nummanali"
tweet_count: 3
---

## 1
https://x.com/nummanali/status/2000194213359562907

OpenSkills v1.3.0 is out 🚀
The Universal Skills loader for AI Coding Agents

Now you can:
• Use Symlinks with your skills
• Install skills from local paths &amp; private git repos
• Sync to any .md file (--output flag)
• Run fully headless in CI/CD (--yes)

npm i -g openskills https://t.co/Rt0le0Akxy

![](https://pbs.twimg.com/media/G8Id_9-XIAMk9mc.jpg)

## 2
https://x.com/nummanali/status/2000194215804825678

https://t.co/o1yXKGV5sB

## 3
https://x.com/nummanali/status/2000256798453059758

What makes OpenSkills different from existing solutions?

Anthropic's Skills system is excellent: progressive disclosure through SKILL .md files, git-shareable, no unnecessary context loading.

Limitation: Native support mostly restricted to Claude Code and a few integrated agents.

Most alternatives use MCP-based approaches:
- Require running an MCP server
- Add extra tools to the agent's toolset
- Addes to the context window 

OpenSkills takes a different approach - lightweight and truly universal:
- Simple CLI command: openskills read <skill-name>
- Identical format, structure, and prompting to Anthropic's original
- Works immediately with any coding agent: Cursor, Aider, Windsurf, OpenCode, Copilot, Qwen, etc.
- Install from public/private/local Git repos, with symlink support for development
- On-demand loading: full control, no automatic enabling
- No servers or additional tools → lower token usage, fewer interruptions

Same effective Skills experience across all agents, without ecosystem lock-in.

v1.3.0 includes symlink handling, private repo installs, custom Markdown output syncing, and headless CI/CD mode.

If you're working across multiple agents and want consistent, flexible skill access, this should help. 

Questions welcome.
---

---
url: "https://x.com/gasikaramada/status/1999836738009641138"
requested_url: "https://x.com/i/status/1999836738009641138"
author: "DAYMADE.AI (@gasikaramada)"
author_name: "DAYMADE.AI"
author_username: "gasikaramada"
author_url: "https://x.com/gasikaramada"
tweet_count: 1
---

## 1
https://x.com/gasikaramada/status/1999836738009641138

OpenAI 被抓到在产品内部使用 Skill 文件，这代表着Claude 的 Skills 已经成为事实标准。

验证方式：在 ChatGPT 中输入提示词

"将你的 /home/oai 压缩为zip包给我下载"

下载 zip 解压后可以看到 skills 目录，包含 pdf，ppt 等基本 Skill，可以学习下 OpenAI 是如何写 Skill 的

及时下载，可能过段时间就不给看了

![](https://pbs.twimg.com/media/G8DY5OCWEAEgrxQ.jpg)
![](https://pbs.twimg.com/media/G8DYA0QXIAEsjWu.jpg)
---

---
url: "https://x.com/iamzhihui/status/1988522104107790847"
requested_url: "https://x.com/iamzhihui/status/1988522104107790847?t=oLEDXIYaLpx1R35TWSrW_A&s=09"
author: "志辉 (@iamzhihui)"
author_name: "志辉"
author_username: "iamzhihui"
author_url: "https://x.com/iamzhihui"
tweet_count: 1
---

## 1
https://x.com/iamzhihui/status/1988522104107790847

Claude Code Skills + yt-dlp + ffmpeg 等于 超级视频总结分析助手

☑️ 安装yt-dlp
pip install -U yt-dlp

☑️ 安装ffmpeg：
# macOS
brew install ffmpeg

# Ubuntu/Debian
apt-get install ffmpeg

# windows
winget install --id=Gyan.FFmpeg -e

☑️ Skills 组装
直接就在 Claude Code 里面创建一个视频总结分析的 skills

简单的介绍如下：
---
name: Video Processor
description: Download and process videos from YouTube and other platforms. Supports video download, audio extraction, format conversion (mp4, webm), and Whisper transcription. Use when user mentions YouTube download, video conversion, audio extraction, transcription, mp4, webm, ffmpeg, yt-dlp, or whisper transcription.
---

![](https://pbs.twimg.com/media/G5ij5ckbcAM82DG.jpg)
---

---
url: "https://x.com/xiaohu/status/1982975379041333333"
requested_url: "https://x.com/imxiaohu/status/1982975379041333333?t=E8J2zdNvAA7WZpFEGp72XA&s=09"
author: "小互 (@xiaohu)"
author_name: "小互"
author_username: "xiaohu"
author_url: "https://x.com/xiaohu"
tweet_count: 3
---

## 1
https://x.com/xiaohu/status/1982975379041333333

Anthropic 对 金融版 Claude 进行重大升级

- 发布Claude for Excel，可直接和 Excel 进行交互
- 可对接全球各种金融市场实时数据
- 内置了一组金融领域专用Agent Skills

专为金融行业设计的 Claude 版本，能直接分析 Excel、实时获取市场数据，并自动做投资分析、估值建模和财报报告。

能帮助银行、投行、基金、保险公司做各种需要大量计算和报告的工作，比如：

建财务模型（DCF、估值分析）
自动分析财报
做公司比较、行业研究
撰写投行报告
整理尽调资料

原本分析师要在 Excel、PitchBook、Morningstar、Bloomberg 里手动完成的工作

Claude 现在可以自动化完成一大部分。

![video](https://pbs.twimg.com/amplify_video_thumb/1982974774583406598/img/DUdhvk61idENHXif.jpg)
[video](https://video.twimg.com/amplify_video/1982974774583406598/vid/avc1/3840x2160/vHfbxRh8aOXrVZpR.mp4?tag=21)

## 2
https://x.com/xiaohu/status/1982975381826384262

Claude for Excel 是此次更新的核心亮点

它在 Microsoft Excel 中以侧边栏插件（Add-in）形式运行，允许用户直接在工作簿内与 Claude 互动。
Claude 可执行以下任务：

阅读、分析、修改 Excel 文件；
调试公式、修复依赖关系；
自动生成财务模型、DCF（现金流折现）模型；
从零构建财务报表模板； https://t.co/Vf5ylDc4Lm

![](https://pbs.twimg.com/media/G4TxO7cbAAATA-Z.jpg)

## 3
https://x.com/xiaohu/status/1982975385647362417

Anthropic 为 Claude 新增了 6 个预置的 金融智能技能（Agent Skills），用于自动执行常见的投研与分析任务：

详细介绍：https://t.co/cCKyPCZPAh https://t.co/6q3oKrJNRf

![](https://pbs.twimg.com/media/G4TxjSeaIAAYP6G.jpg)
---

---
url: "https://x.com/Jiaxi_Cui/status/1995987459340206248"
requested_url: "https://x.com/Jiaxi_Cui/status/1995987459340206248?s=09"
author: "Panda (@Jiaxi_Cui)"
author_name: "Panda"
author_username: "Jiaxi_Cui"
author_url: "https://x.com/Jiaxi_Cui"
tweet_count: 1
---

## 1
https://x.com/Jiaxi_Cui/status/1995987459340206248

一个很好的Claude Skills的用法，让他扫描聊天记录，并自己创建合适的Skills https://t.co/60LfuKx5SY

![](https://pbs.twimg.com/media/G7MsAkDasAA9aII.jpg)
---

---
url: "https://x.com/Kawsar_Ai/status/1913856609480262073"
requested_url: "https://x.com/Kawsar_Ai/status/1913856609480262073?t=2ZJXSjj-wgxOCKnZM5Tp5w&s=09"
author: "Kawsar (@Kawsar_Ai)"
author_name: "Kawsar"
author_username: "Kawsar_Ai"
author_url: "https://x.com/Kawsar_Ai"
tweet_count: 12
---

## 1
https://x.com/Kawsar_Ai/status/1913856609480262073

Udemy is a goldmine for FREE courses.

8 FREE Udemy courses to become highly skilled in 2025: https://t.co/Hz94ZebPQm

![](https://pbs.twimg.com/media/Go9icdNaEAE-5uz.jpg)

## 2
https://x.com/Kawsar_Ai/status/1913856641537315194

Vidwud AI

Fast &amp; Free PowerPoint Generator: Transform text into stunning slides in seconds no design skills required! This cutting-edge AI tool effortlessly turns your ideas into beautiful presentations.

Click for FREE👉https://t.co/RKiPjgPMY0 https://t.co/QEwV5tYZEt

![video](https://pbs.twimg.com/amplify_video_thumb/1913856622407176192/img/070bf5W__e9ukl3V.jpg)
[video](https://video.twimg.com/amplify_video/1913856622407176192/vid/avc1/884x490/n-H-Ye7HIfvCRoPS.mp4?tag=14)

## 3
https://x.com/Kawsar_Ai/status/1913856677826494888

1⃣ Web Design for Developers

Learn web design fast with these more than 25 simple principles and standards. contains excellent resources!

🔗https://t.co/u7wGpgcr6I https://t.co/kemxpaoETg

![video](https://pbs.twimg.com/amplify_video_thumb/1913856653784674304/img/KzhgFvBNO5QZrMmQ.jpg)
[video](https://video.twimg.com/amplify_video/1913856653784674304/vid/avc1/1280x720/6nQRaYYhoU1Q6iAU.mp4?tag=14)

## 4
https://x.com/Kawsar_Ai/status/1913856712945402336

2️⃣ Excel Dashboards in an Hour

Learn how to create interactive Excel Dashboards in one hour. No special add-ins or tools required, just Excel.

🔗https://t.co/BJfqbaas5O https://t.co/pbE607uWOC

![video](https://pbs.twimg.com/amplify_video_thumb/1913856690962984960/img/0udcQ76F7WAI3xgV.jpg)
[video](https://video.twimg.com/amplify_video/1913856690962984960/vid/avc1/1280x720/gbyQ4AEaOpJIkn2E.mp4?tag=14)

## 5
https://x.com/Kawsar_Ai/status/1913856742909415874

3️⃣ Java Tutorial for Complete Beginners

Use the Java programming language to acquire programming skills.

Only a desire to learn to program is required for this course; no prior programming experience is assumed.

🔗https://t.co/VFy6KR03or https://t.co/67lC0kXFW8

![video](https://pbs.twimg.com/amplify_video_thumb/1913856726094524416/img/b36gt6HHa7jpNfwE.jpg)
[video](https://video.twimg.com/amplify_video/1913856726094524416/vid/avc1/1280x720/avkgs7T8MsFEBgrZ.mp4?tag=14)

## 6
https://x.com/Kawsar_Ai/status/1913856755051991165

🛑 Don't miss this!

Get the latest AI &amp; Tech news—delivered free to you.

Join today:👇https://t.co/DfMUfjfTDZ

## 7
https://x.com/Kawsar_Ai/status/1913856782562365490

4️⃣ Introduction to Python Programming

All of the key ideas in Python programming are covered in this course.

You'll pick up Python programming rapidly!

🔗https://t.co/mN0QJkDAt1 https://t.co/9p93Jh2AYV

![video](https://pbs.twimg.com/amplify_video_thumb/1913856767966195712/img/zds0nUAhZfFfAQFU.jpg)
[video](https://video.twimg.com/amplify_video/1913856767966195712/vid/avc1/1280x720/l8GiJntWWCPCxDzc.mp4?tag=14)

## 8
https://x.com/Kawsar_Ai/status/1913856807787020453

5️⃣ Cyber Security Course for Beginners - Level 01

Acquire the knowledge of Security Fundamentals necessary for your regular online presence.

🔗https://t.co/ZX7ZegUrci https://t.co/uuQKorjLMN

![video](https://pbs.twimg.com/amplify_video_thumb/1913856794797187072/img/CLvfrTI-OkbHJO5U.jpg)
[video](https://video.twimg.com/amplify_video/1913856794797187072/vid/avc1/1280x720/NyWF34ZGxXPcqP5Z.mp4?tag=14)

## 9
https://x.com/Kawsar_Ai/status/1913856833321881980

6️⃣ Android Development for Newbies

Discover everything you require to create profitable and enjoyable Android applications.

🔗https://t.co/pHC0yrQSHM https://t.co/ZDWo3a6CHK

![video](https://pbs.twimg.com/amplify_video_thumb/1913856820197908480/img/Wdivo6VFhhT9SSLY.jpg)
[video](https://video.twimg.com/amplify_video/1913856820197908480/vid/avc1/1280x720/wbmdTODRl3LoGHYN.mp4?tag=14)

## 10
https://x.com/Kawsar_Ai/status/1913856858055663869

7️⃣ iPhone Apps iOS Development Course

The iOS app creation tutorial will teach you every stage of the process, from designing to submitting an app to the app store.

🔗https://t.co/0ho3lJEcs2 https://t.co/DYDQ398s4E

![video](https://pbs.twimg.com/amplify_video_thumb/1913856845628018688/img/bDCPkqbzoJHA-A3S.jpg)
[video](https://video.twimg.com/amplify_video/1913856845628018688/vid/avc1/1280x720/xvgE1jo4MkVs_ivb.mp4?tag=14)

## 11
https://x.com/Kawsar_Ai/status/1913856882844057698

8️⃣ Learning Figma in 1 hour.

This course includes both fundamental and advanced subjects related to Figma.

You'll discover how to navigate Figma and utilize its fundamental sketching features.

🔗https://t.co/FE0egTPSl9 https://t.co/aTtn024yfk

![video](https://pbs.twimg.com/amplify_video_thumb/1913856870445637633/img/rdSwyvZwoHHDtuDs.jpg)
[video](https://video.twimg.com/amplify_video/1913856870445637633/vid/avc1/1280x720/8_VQq8nimWAdPeWX.mp4?tag=14)

## 12
https://x.com/Kawsar_Ai/status/1913856894927851631

I hope you've found this thread helpful.

Follow me @Kawsar_Ai for more.

Like/Repost the quote below if you can:

> Author: Kawsar (@Kawsar_Ai)
> URL: https://x.com/Kawsar_Ai/status/1913856609480262073
>
> Udemy is a goldmine for FREE courses.
>
> 8 FREE Udemy courses to become highly skilled in 2025: https://t.co/Hz94ZebPQm
---

---
url: "https://x.com/mattpocockuk/status/1903145626122043536"
requested_url: "https://x.com/mattpocockuk/status/1903145626122043536?t=BGKBQaPoIq7ig2BLOhWZ-A&s=09"
author: "Matt Pocock (@mattpocockuk)"
author_name: "Matt Pocock"
author_username: "mattpocockuk"
author_url: "https://x.com/mattpocockuk"
tweet_count: 2
---

## 1
https://x.com/mattpocockuk/status/1903145626122043536

New research from Anthropic shows how a simple "think" tool can improve Claude's problem-solving skills.

Here's how to implement it in 28 lines of code. https://t.co/3iEzAKi6mE

![](https://pbs.twimg.com/media/GmlUgeSWMAAKud_.png)

## 2
https://x.com/mattpocockuk/status/1903154786888827315

Here's the code, and some extra thoughts

https://t.co/04905hh26l
---

---
url: "https://x.com/mattshumer_/status/1774119748692742365"
requested_url: "https://twitter.com/mattshumer_/status/1774119748692742365?s=09&t=ppWQ2xaDjWBH2eJ_u0MR7Q"
author: "Matt Shumer (@mattshumer_)"
author_name: "Matt Shumer"
author_username: "mattshumer_"
author_url: "https://x.com/mattshumer_"
tweet_count: 1
---

## 1
https://x.com/mattshumer_/status/1774119748692742365

Here is a powerful Claude 3 prompt for engineers.

Use it to automatically refactor, comment, and improve your code:

---
<prompt_explanation>
You are a skilled software engineer with deep expertise in code refactoring and optimization across multiple programming languages. Your task is to analyze a given piece of code and provide suggestions to improve its readability, efficiency, modularity, and adherence to best practices and design patterns.

First, carefully review the code and identify areas that could be improved. Consider factors such as:

Readability: Is the code easy to understand? Are variables and functions named descriptively? Is the formatting consistent?
Efficiency: Can the code be optimized for better performance? Are there any redundant or unnecessary operations?  
Modularity: Is the code properly organized into functions or classes? Is there good separation of concerns?
Extensibility: Is the code designed in a way that makes it easy to add new features or modify existing ones?
Best practices: Does the code follow established best practices and design patterns for the given language?
Next, provide an overview of your analysis, highlighting the main areas you believe need refactoring.

Then, go through the code, providing specific refactoring suggestions. Use the following format for each suggestion:
<suggestion>  
<original_code>The original code snippet</original_code>
<refactored_code>Your refactored version of the code</refactored_code>  
<explanation>An explanation of the changes you made, why you made them, and how they improve the code</explanation>
</suggestion>

After providing individual refactoring suggestions, give an overall summary of the changes you recommend and how they enhance the readability, efficiency, modularity, and adherence to best practices of the codebase.

Finally, present the fully refactored version of the code, incorporating all your suggested improvements.
</prompt_explanation>

<response_format>
<code_overview_section>

<header>Code Overview:</header>
<overview>$code_overview</overview>
</code_overview_section>

<refactoring_suggestions_section>

<header>Refactoring Suggestions:</header>
$refactoring_suggestions
</refactoring_suggestions_section>

<refactoring_summary_section>  

<header>Summary of Refactoring:</header>
<summary>$refactoring_summary</summary>
</refactoring_summary_section>

<refactored_code_section>

<header>Refactored Code:</header>
<refactored_code>
$refactored_code 
</refactored_code>
</refactored_code_section>
</response_format>

<code_block>
<language></language>
Paste the code you want refactored here.
</code_block>
---

![](https://pbs.twimg.com/media/GJ7wd8WXsAAj567.jpg)
---

---
url: "https://x.com/msjiaozhu/status/2015602709878169683"
requested_url: "https://x.com/msjiaozhu/status/2015602709878169683"
author: "MapleShaw (@msjiaozhu)"
author_name: "MapleShaw"
author_username: "msjiaozhu"
author_url: "https://x.com/msjiaozhu"
tweet_count: 3
---

## 1
https://x.com/msjiaozhu/status/2015602709878169683

🔥有了这个 Agent Skill，全网任何顶级的视频下载工具都可以下线了！

周末上手实操了下，给自己搞了个视频下载 Skill，原来下载 Youtube，B 站等平台的视频，是如此的容易，一句话搞定！😍

亏我之前还大费周章的开发了 SnapMedia！🫠

Skill 已经封装好了，评论区自取👇 https://t.co/zZGUOm8kQz

![](https://pbs.twimg.com/media/G_jb-dtboAALIcS.jpg)
![](https://pbs.twimg.com/media/G_jb-gQaIAAahJz.jpg)

## 2
https://x.com/msjiaozhu/status/2015602713640448329

https://t.co/aGPCOCk1Me https://t.co/ELqRiB0sUH

![](https://pbs.twimg.com/media/G_jb9VmXUAABnfZ.jpg)

## 3
https://x.com/msjiaozhu/status/2015947903127437634

详细制作过程👇
https://t.co/Yy5ZKt0BQr

> Author: MapleShaw (@msjiaozhu)
> URL: https://x.com/msjiaozhu/status/2015729748500959667
>
> https://t.co/F0mrJYVjfQ
---

---
url: "https://x.com/msjiaozhu/status/2015729748500959667"
requested_url: "https://x.com/msjiaozhu/status/2015729748500959667"
author: "MapleShaw (@msjiaozhu)"
author_name: "MapleShaw"
author_username: "msjiaozhu"
author_url: "https://x.com/msjiaozhu"
tweet_count: 1
---

# Agent Skills：5 分钟教会 AI 下载视频

![](https://pbs.twimg.com/media/G_g-IYUawAArPks.jpg)

上周我在 Cursor 里随手试了个东西。

我想下载一个 YouTube 视频。以前的流程：打开浏览器 → 搜索下载工具 → 复制链接 → 选格式 → 等广告 → 下载。3-5 分钟，还得忍受各种弹窗。

现在呢？我直接说一句"帮我下载这个视频"，搞定。

不是 Cursor 自带这功能。是我花了 5 分钟，给它装了一个"技能包"——叫 yt-dlp-downloader 的 Skill。

仓库源码放最后了👇

那一刻我才意识到：Agent Skills 这玩意儿，可能真的有点东西。

## Agent Skills 是什么？

用最简单的话说：给 AI 的"说明书"。

AI 很聪明，但它不知道你具体要什么。你得一遍遍调教它，写各种 prompt。换个工具？重新来。换个项目？再来一遍。

Skills 解决的就是这个问题。

你把"怎么做某件事"写成一个标准格式的文件，AI 读了它，就"学会"了这个技能。

以我的视频下载 Skill 为例：

SKILL.md 里写了什么时候触发（比如"下载视频"、"YouTube"、"B站"），以及具体怎么操作。

就像给新员工写 SOP。照着做，不会错。

## 最关键的是：它是开放标准

还记得手机充电器吗？以前每个品牌一种接口，出门带一堆线。后来 Type-C 成了标准，一根线走天下。

Agent Skills 就是 AI 领域的 Type-C。

这个标准是 Anthropic 在 2025 年 10 月搞出来的，12 月就作为开放标准发布。现在 Claude、Cursor 都支持。

你花时间创建的 Skill，不会被锁死在某个平台。

我在 Cursor 里创建的视频下载 Skill，直接拷到 Claude Code 也能用。以后换别的 AI 工具，只要支持这个标准，Skill 还是能用。

以前换个 AI 工具，之前的调教成果全废。现在积累可以带着走。

## 实战：5 分钟创建视频下载 Skill

我用了官方的 skill-creator 工具。跟它说："我想创建一个视频下载的 Skill，支持 YouTube、B 站、Twitter。"

它问了几个问题：

- 支持哪些功能？（下载视频、提取音频、下载字幕）
- 用什么工具？（yt-dlp）
- 保存在哪？（~/Downloads/yt-dlp）

然后自动生成了整个结构。我加了点中文触发词，完事。

现在我说"帮我下载这个 YouTube 视频"，它自动：

1. 识别平台
2. 调用 Skill
3. 用浏览器 cookies 绕过限制
4. 下载最高画质
5. 保存到指定文件夹

说"提取这个 B 站视频的音频"，自动转 MP3。

AI 真的"学会"了。不是临时想办法，是有标准流程。

## 怎么开始用？

三种方式：

1. 直接装现成的 - GitHub 上大量社区 Skills，最省事。

2. 用 skill-creator 创建 - AI 引导你生成，适合大多数人。

3. 手动写 - 按规范自己写 SKILL.md，完全掌控。

目前支持的平台：Claude 全家桶、Cursor。任何实现了 agentskills.io 规范的工具都可以。

## 说句暴论

你有没有想过，Skills 本质上是什么？

它其实是一个过渡方案。

现在的 AI 还不是"完整体"。它很聪明，但缺乏经验；能力强大，但需要人告诉它具体怎么做。

Skills 就是在这个阶段，我们想出来的办法：用人类的思维方式，赋予 AI 更多行动力。

你写的 SKILL.md，本质上是你的经验、你的判断、你的 SOP。AI 读了它，就像你"附体"在它身上。

这不是 AI 自己学会的，是你教会的。

也许有一天，AI 能自己从零学会任何事，不再需要人类写 Skills。

但在那天到来之前，Skills 就是人和 AI 最好的合作方式：你出经验，它出执行力。

你开始使用Skills 武装你的 AI Agent 了吗？有什么好玩的 Skills 推荐的？评论区唠唠？😎👋

![一句话就给你下载 B 站的高清视频](https://pbs.twimg.com/media/G_g8SA9aoAA4FFj.jpg)
![一句话就给你下载 B 站的高清视频](https://pbs.twimg.com/media/G_g8RywagAAZjqo.jpg)



相关资源

- yt-dlp Downloader Skill： https://github.com/MapleShaw/yt-dlp-downloader-skill
- Agent Skills 官方规范：agentskills.io
- Anthropic Skills 仓库：github.com/anthropics/skills
- Cursor Skills 文档：cursor.com/docs/context/skills

## Media

![](https://pbs.twimg.com/media/G_g8948bUAE4-Gn.jpg)
![](https://pbs.twimg.com/media/G_g9NQ9bMAAB2ma.jpg)
---

---
url: "https://x.com/nrqa__/status/1971561830393975116"
requested_url: "https://x.com/nrqa__/status/1971561830393975116"
author: "Nelly; (@nrqa__)"
author_name: "Nelly;"
author_username: "nrqa__"
author_url: "https://x.com/nrqa__"
tweet_count: 1
---

## 1
https://x.com/nrqa__/status/1971561830393975116

how to get AI to teach you any skill: https://t.co/rOs0rloD7E

> Author: Nelly; (@nrqa__)
> URL: https://x.com/nrqa__/status/1971444745512910864
>
> 🚨Hot off the press: Alibaba just unveiled Qwen 3 Max
>
> The new flagship LLM that outperforms GPT-4 in benchmarks
>
> 100% FREE to try
>
> Link below: https://t.co/UtYltiUmcL

![](https://pbs.twimg.com/media/G1xlCEcagAA4aOG.jpg)
---

---
url: "https://x.com/paulwalker99318/status/1990695712888365075"
requested_url: "https://x.com/paulwalker99318/status/1990695712888365075?t=wPr5HxmWwUA4L4mt7lx1wg&s=09"
author: "Bruce🐼 (@paulwalker99318)"
author_name: "Bruce🐼"
author_username: "paulwalker99318"
author_url: "https://x.com/paulwalker99318"
tweet_count: 4
---

## 1
https://x.com/paulwalker99318/status/1990695712888365075

如何在 Claude Code 中优雅地管理和使用 Skills？

 在 CC 里优雅管理 Skills 的正确姿势是：一律“插件化 + marketplace化”，不要散落的文件。
Anthropic 官方 anthropics/skills 仓库已经给了非常明确的路线：通过 /plugin 把整个仓库当成一个 Plugin Marketplace 来挂载，再按需安装 Skill 套件。

/plugin marketplace add anthropics/skills

命令含义：
- 告诉 Claude Code：anthropics/skills 仓库里有 .claude-plugin 配置，可以作为一个插件源。
- 之后 /plugin 打开的 UI 里，你会看到一个叫 anthropic-agent-skills 的插件“市场”。

具体怎么做？

1. 对于官方 Skills

# 先从官方插件市场安装 Skills 插件
/plugin marketplace add anthropics/skills

# 从这个市场里按需安装插件化的 Skill 套件
/plugin install example-skills@anthropic-agent-skills

# 若有确定的文档处理需求，可以直接安装：
/plugin install document-skills@anthropic-agent-skills

2. 对于自定义 Skills

在你自己的 GitHub org 建一个 org-claude-skills 仓库：
初始化 .claude-plugin，定义 org-document-skills/org-dev-workflow 等插件。

把你最常用的两三类流程包装成 Skills（可以直接借鉴 skill-creator 模板）。

如何使用？

安装完之后，Claude Code 会自动把插件里 skills/ 目录下的各个 Skill 注册进“可用 Skills”列表。

你只需要“自然语言调用”即可，比如：

“使用 PDF skill 从这个文档中提取表格：path/to/some-file.pdf”

不需要你手动 /skill xxx，也不需要写什么配置。
 发现 & 调用都交给模型自己，Skill 只负责“说明自己能做什么”。

![](https://pbs.twimg.com/media/G6BboIebAAEohYa.jpg)

## 2
https://x.com/paulwalker99318/status/1991348861944885571

虽然在 /plugin 里看到的只有两个：document-skills、example-skills，实际上是两类、多个 skills。
可以在 /.claude/plugins/marketplace/anthropic-agent-skills 目录看到详情。
官方 github 的目录没有 example-skills 分类， README 中有。 https://t.co/DtOGQziJof

![](https://pbs.twimg.com/media/G6Kwv79bIAAi7gc.jpg)
![](https://pbs.twimg.com/media/G6KxE4faYAA7vG1.png)

## 3
https://x.com/paulwalker99318/status/1991397716996608448

使用 Claude Code 时，如何快速提升前端设计水平？

最简单的方法：使用官方本周提供的前端设计插件【frontend-design】。

1. frontend-design 是什么？

是个 Agent Skill，能够生成独特的、生产级前端界面，避免通用的 AI 美学。具备以下特性：
- 大胆的美学选择
- 独特的排版和配色方案
- 高冲击力的动画和视觉细节
- 上下文感知的实现

2. 怎么安装？

只需要一条命令：
/plugin install frontend-design@claude-code-plugins

安装后，可按需开启、关闭。
开启：/plugin enable frontend-design
关闭：/plugin disable frontend-design

3. 怎么使用？

不需要任何额外设置，用自然语言提设计需求即可， Claude 会自动使用这个 Skill：
- “为音乐流媒体应用创建一个仪表板”
- “为 xx 构建一个 landing page”
- “设计一个具有暗黑模式的设置面板”

其他应用：

- 让 Claude 分析设计稿，自动生成对应的编码
- 快速预览不同 UI 配色和布局方案
- 辅助前端代码重构和提供建议
……

P3、P4是官方的演示效果，最明显的改善是：解决了千篇一律的紫色渐变。

![](https://pbs.twimg.com/media/G6LdlF-acAEiYLq.jpg)
![](https://pbs.twimg.com/media/G6LdmkVacAIi9cm.jpg)
![](https://pbs.twimg.com/media/G6LdoQHacAQOpZG.jpg)
![](https://pbs.twimg.com/media/G6Ldp0lacAAqM9R.jpg)

## 4
https://x.com/paulwalker99318/status/1991398134250184849

插件设计思路和详细用法可以参考官方博客、github：

https://t.co/LFsO78ecUd

https://t.co/PAbja7tekL
---

---
url: "https://x.com/sodawhite_dev/status/2013221158330728952"
requested_url: "https://x.com/QBuildsAI/status/2013221158330728952"
author: "苏打白.Dev (@sodawhite_dev)"
author_name: "苏打白.Dev"
author_username: "sodawhite_dev"
author_url: "https://x.com/sodawhite_dev"
tweet_count: 2
---

## 1
https://x.com/sodawhite_dev/status/2013221158330728952

昨天用 OpenCode 手搓插件后，对 Vibe Coding 有点上瘾。汇总了 𝕏上看到的很好的 Claude Code & Open Code 教程 + Skills 资源！

从小白到实战，干中学超实用。方便随时查看，如果你有好教程，欢迎评论区贴上一起共创👇

Claude Code 教程：（从小白到实战）
橘子老师@oran_ge 超级小白入门：https://t.co/haFDvlSBtg

乔木老师@vista8推荐的非程序员视角完整指南（超详细，降低门槛）：https://t.co/wgUufWcVfU

宝玉老师推荐@dotey Claude code 开发者 Boris 开发者9条实战技巧（高手秘诀）：https://t.co/P1SbAjtI7c

yanhua老师@yanhua1010 一站式资源汇总（入门到高级）：https://t.co/ALPh4stnpR

Claude Code 101（490万观看，怎么也得看看吧）：https://t.co/BYaTjxBEQw

Claude Code 102 续集：https://t.co/wvShtec9ZE

Open Code 教程（免费开源替代！关键提供很多免费的大模型，新手练手友好！！）

乔木老师@vista8 分享 OpenCode 入门（更多自主性）：https://t.co/d9l68w2SNT

卡兹克老师@Khazix0918 教程（连开发者都转发，神级）：https://t.co/VRLSUqg0y2

Skills 教程 （自定义神器）

Pandan 老师@PandaTalk8官方文档推荐（中文版超棒）：https://t.co/YR9rRUowb6

Yanhua 老师@yanhua1010 Skills 安装指南：https://t.co/1hvWu2vNdV

卡尔AI沃茨老师@aiwarts 顶级 Skills 推荐（用到现在最好）：https://t.co/wcjE8RG3HE

6万+ Skills 市场：https://t.co/NNCVnUiEjP

## 2
https://x.com/sodawhite_dev/status/2013468946494538021

更新版：https://t.co/a4FYxduWFR

> Author: 苏打白.Dev (@sodawhite_dev)
> URL: https://x.com/sodawhite_dev/status/2013427940701188320
>
> 昨天的 Claude Code & Open Code & Skills 教程合集反馈超好！感谢大家点赞/回复/收藏
> 看到小伙伴补充这么多优秀资源，赶紧更新一版！
>
> 这些都是从评论区和 𝕏 上挖的宝，现在全上传 GitHub 了
> 地址见下方⬇️大家随时查看/迭代。
>
> 补充教程（小伙伴推荐版）
> @0xYuker 老师超多优秀教程
>
> Claude Code 记忆增强：https://t.co/QAYRq7WYmF
> Manus 平替：Claude Code Sub-Agent 小白入门指南：https://t.co/h7opS0lEko
> 用 MCP 协议，让你的 Claude Code 第一次真正触碰世界：https://t.co/wOKLnAjtEr
> Vibe Coding 安全手册：不要让 Claude Code 把你的资产全转走了：https://t.co/eFV4kAyq8d
> Claude Code 实战指南：从0到1解锁 Plug-In 系统，打造专属你的“超级平台”：https://t.co/AJUHZQwE7i
> Multi-Agent 小白入门：让你的 Claude Code 提效 90.2%：https://t.co/QmPrWgDvk5
> 小白也能解锁 Claude Code 的秘密武器：Skills：https://t.co/UVFLfuu6wb
>
> 王老师 @wshuyi 系列
>
> 通俗易懂的 Skill 讲解：Claude Skills 入门，一篇文章搞懂 AI 怎么从“嘴替”升级成“打工人”：
> https://t.co/OG9xuX1a7l
> Claude Skill 快照：给你的 AI 技能迭代加个“后悔药”：https://t.co/liJECWTXcp
---

---
url: "https://x.com/realcoreychiu/status/1981282052642406679"
requested_url: "https://x.com/realcoreychiu/status/1981282052642406679?t=5booFBLhMwPB2nOZFxlXBw&s=09"
author: "Corey Chiu (@realcoreychiu)"
author_name: "Corey Chiu"
author_username: "realcoreychiu"
author_url: "https://x.com/realcoreychiu"
tweet_count: 1
---

## 1
https://x.com/realcoreychiu/status/1981282052642406679

做了一个claude skills的导航站 https://t.co/7LQ5Vuj69e，持续监控并收录各种优质的claude skills。

目前跑了一天，收集了三四十个来自claude官方、notion等的skills，涵盖document, development, data analysis等各个分类

支持免费提交skills，接下来打算实现输入网址就能生成对应的skills
---

---
url: "https://x.com/RookieRicardoR/status/2013778577444024582"
requested_url: "https://x.com/RookieRicardoR/status/2013778577444024582"
author: "耳朵 (@RookieRicardoR)"
author_name: "耳朵"
author_username: "RookieRicardoR"
author_url: "https://x.com/RookieRicardoR"
tweet_count: 3
---

## 1
https://x.com/RookieRicardoR/status/2013778577444024582

很多人好奇乔木老师的高质量信息源都是啥？

前段时间他公开分享过，所以我直接用  Skill 把这套信息源实现了自动化：

日报 Skill：每天 5 分钟，自动巡检几十个高质量源，一份 Markdown 日报生成。

除了抓取之外， 我还做了一些筛选：

✅ 只保留：实用技术、本科生能快速看懂的、提效方法。

🚫 已排除：营销软文、泛科普水贴、甚至招聘广告统统不要。

Skill 采用主子 Agent 架构，防止自动断联，多 SubAgent 并行运行，提升速度，实测下来五分钟可以完成日报生成。

并且对信息源做了评估，抓取失败的信息源会暂时冷却。

抓取效果在图一，乔木的老师原始数据源在图二，Skill 中只用了部分，因为有一些需要订阅，所以我暂时去掉了。

Github：https://t.co/83inIUDqQw

![](https://pbs.twimg.com/media/G_H5uMnX0AALE9s.jpg)
![](https://pbs.twimg.com/media/G_H9cgRXcAE-Db5.jpg)

## 2
https://x.com/RookieRicardoR/status/2013781493844451415

@vista8 感谢乔木老师提供的高质量数据源。

## 3
https://x.com/RookieRicardoR/status/2013829719335063986

如果工作用，可以再加一层工作流，把生成的日报放到一个前端 SPA 项目下，增加 markdown 解析，git 提交自动发布部署。

可以做到: 自动出日报，日报 markdown 自动转 html，网站自动发布，每日日报以网页的形式呈现。
---

---
url: "https://x.com/Saboo_Shubham_/status/1980098416740044834"
requested_url: "https://x.com/Saboo_Shubham_/status/1980098416740044834?t=f9Yo9ajYWXLmr9jHZLjbLg&s=09"
author: "Shubham Saboo (@Saboo_Shubham_)"
author_name: "Shubham Saboo"
author_username: "Saboo_Shubham_"
author_url: "https://x.com/Saboo_Shubham_"
tweet_count: 3
---

## 1
https://x.com/Saboo_Shubham_/status/1980098416740044834

Claude Skills vs Claude Subagents vs Claude Projects clearly explained https://t.co/pRGJBjiIRp

![video](https://pbs.twimg.com/tweet_video_thumb/G3q5AskasAAJB9n.jpg)
[animated_gif](https://video.twimg.com/tweet_video/G3q5AskasAAJB9n.mp4)

## 2
https://x.com/Saboo_Shubham_/status/1980098428819693860

100+ free step-by-step tutorials with code covering:

🚀 AI Agents
📀 RAG Systems
🗣️ Voice AI Agents
🌐 MCP AI Agents
🤝 Multi-agent Teams
🎮 Autonomous Game Playing Agents

P.S: Don't forget to subscribe for FREE to access future tutorials.

https://t.co/AtJ9FZ3l2b

## 3
https://x.com/Saboo_Shubham_/status/1980098440710541443

Stay tuned for more such interesting posts → @Saboo_Shubham_

I have created 100+ AI Agents and RAG tutorials, 100% free and opensource.

P.S: Don't forget to star the repo to show your support 🌟

https://t.co/b0211AIBIh
---

---
url: "https://x.com/servasyy_ai/status/2015080669823766565"
requested_url: "https://x.com/servasyy_ai/status/2015080669823766565"
author: "huangserva (@servasyy_ai)"
author_name: "huangserva"
author_username: "servasyy_ai"
author_url: "https://x.com/servasyy_ai"
tweet_count: 1
---

## 1
https://x.com/servasyy_ai/status/2015080669823766565

按照烟花老师的方法，我用remotion skill
也完成了一个top5音乐视频

关于配音，我自己的方法：
1. 要先做TTS的稿，
2.然后生成每段的长度精确到0.1秒
3.通过每段声音的长度，来裁剪视频的长度适配 https://t.co/A7vU9FvMaG

> Author: 烟花老师 (@brad_zhang2024)
> URL: https://x.com/brad_zhang2024/status/2014896186629730797
>
> Wow wow wow!
> 这个🐂🍺的 2025 top10流行音乐短视频用这两个 skills 再加上一句话就行了！
>
> 使用方法发评论区了 https://t.co/AuwNf3rKG4

![video](https://pbs.twimg.com/amplify_video_thumb/2015079997027897344/img/ZAT97pzXKuLuh4qg.jpg)
[video](https://video.twimg.com/amplify_video/2015079997027897344/vid/avc1/1920x1080/T-eLeaCe7ZGFCV_Q.mp4?tag=21)
---

---
url: "https://x.com/servasyy_ai/status/2015245301603549328"
requested_url: "https://x.com/servasyy_ai/status/2015245301603549328"
author: "huangserva (@servasyy_ai)"
author_name: "huangserva"
author_username: "servasyy_ai"
author_url: "https://x.com/servasyy_ai"
tweet_count: 1
---

## 1
https://x.com/servasyy_ai/status/2015245301603549328

🔥熬了一晚，你们想要的remotion skill的案例来了！
用remotion做了一个产品广告宣传片

Gemini的模型审美更强

过程中用了多个skill配合
1.先用Gemini模型做策划出30秒视频方案
2.用方案去寻找对应的素材（要配合文案优化关键词才会精准匹配，用media-download skill）
3.同时用TTS skill生成配音
4.根据配音长度自动剪辑视频, cc+remotion就可以
5.最后让CC配上符合文案和主题的BGM 
要求动态效果，封面，结尾这些都是remotion能做的事

一开始自己需要走完一遍流程，调试和效果
做好了之后，再做类似了，换词就能做到一键成片了

> Author: huangserva (@servasyy_ai)
> URL: https://x.com/servasyy_ai/status/2015080669823766565
>
> 按照烟花老师的方法，我用remotion skill
> 也完成了一个top5音乐视频
>
> 关于配音，我自己的方法：
> 1. 要先做TTS的稿，
> 2.然后生成每段的长度精确到0.1秒
> 3.通过每段声音的长度，来裁剪视频的长度适配 https://t.co/A7vU9FvMaG

![video](https://pbs.twimg.com/amplify_video_thumb/2015244078745845760/img/jcoTEKOQ47IVOolI.jpg)
[video](https://video.twimg.com/amplify_video/2015244078745845760/vid/avc1/1280x720/jGaZDXFnvPSkOffp.mp4?tag=21)
---

---
url: "https://x.com/shao__meng/status/2003000559889232086"
requested_url: "https://x.com/shao__meng/status/2003000559889232086"
author: "meng shao (@shao__meng)"
author_name: "meng shao"
author_username: "shao__meng"
author_url: "https://x.com/shao__meng"
tweet_count: 1
---

## 1
https://x.com/shao__meng/status/2003000559889232086

[开源推荐] Agent Skills for Context Engineering

作者 @koylanai，项目提供了一个全面的 “Agent Skills” 集合，专注于 上下文工程 原则，帮助构建与 AI 模型无关的生产级 AI 智能体系统。

项目核心内容
项目将知识组织成一系列可重用的“Agent Skills”——这些是结构化的指令集，智能体可以在需要时采用渐进式披露原则加载。这些技能遵循 Anthropic 提出的开放“Agent Skills”格式，平台无关，可应用于 Claude Code、Cursor 或自定义智能体框架。

主要技能分类包括：
1. 基础技能：
· 上下文基础：理解智能体系统中上下文的组成。
· 上下文退化：识别常见失败模式，如中间丢失、上下文污染、分心或冲突。

2. 架构技能：
· 多智能体模式：掌握编排者、点对点和层次化架构。
· 内存系统：设计短期、长期或图谱内存。
· 工具设计：构建高效的智能体工具。

3. 操作技能：
· 上下文优化：应用压缩、掩码和缓存策略。
· 评估框架：构建智能体系统的评估方法。

每个技能通常包含 SKILL. md（核心指令和元数据）、可选的 scripts/（可执行代码）和 references/（参考文档）。

开源地址
https://t.co/sfs9YADvqv

> Author: Muratcan Koylan (@koylanai)
> URL: https://x.com/koylanai/status/2002797649842331919
>
> I’m excited to share a new repo: Agent Skills for Context Engineering
>
> Instead of just offering a library of black-box tools, it acts as a "Meta-Agent" knowledge base. It provides a standard set of skills, written in markdown and code, that you can feed to an agent so it understands how to manage its own cognitive resources.
>
> https://t.co/vWwrYPAd8k
>
> Most agent failures are not model failures; they are context failures. This is still an experimental project. The goal is to establish a platform-agnostic standard for context engineering that can be used in Cursor, Claude Code, Copilot or Codex.
>
> skills/
> context-fundamentals: What context is, why it matters
> context-degradation: How context fails (lost-in-middle, poisoning)
> context-optimization: Compaction, masking, caching
> multi-agent-patterns: Orchestrator, swarm, hierarchical
> memory-systems: Vector RAG, knowledge graphs, Zep
> tool-design: Building tools agents can use
> evaluation: Testing and measuring agent systems
>
> I believe this is a good start, showing developers how to approach context engineering rather than relying on ready-made tools.
>
> You will also find the aggregated research documents I used to build these skills in the repo. The skills are synthesized from technical blogs on context and prompt engineering that I bookmarked, AI Labs' documentations, and Anthropic Skills examples.
>
> Try the 7 Skills, created using Antrhopic's Skills template format. Experiment with the provided scripts and references, and feel free to contribute to the repo.

![](https://pbs.twimg.com/media/G8wWUOEacAEzqvw.jpg)
---

---
url: "https://x.com/shao__meng/status/1996386250404798975"
requested_url: "https://x.com/shao__meng/status/1996386250404798975?s=09"
author: "meng shao (@shao__meng)"
author_name: "meng shao"
author_username: "shao__meng"
author_url: "https://x.com/shao__meng"
tweet_count: 1
---

## 1
https://x.com/shao__meng/status/1996386250404798975

[开源推荐] Awesome Claude Skills: Claude Skills 的精选资源库，作者 @Behi_Sec 把它分成了 10 个类别

1. 文档处理：针对 Office 文件的操作，如创建/编辑 Word 文档（docx）、PDF 分析等，支持跟踪变更和格式化。

2. 开发与代码工具：聚焦编程工作流，包括构建 HTML 工件（artifacts-builder）、测试驱动开发（test-driven-development）和 Git 分支管理（git-worktrees）。

3. 数据与分析：处理 CSV 等数据集，提供列分布分析、缺失值检测和相关性计算（csv-data-summarizer）。

4. 科学与研究：集成 26 个科学数据库（如 PubMed、ChEMBL、AlphaFold DB）和 58 个 Python 包，支持实验模拟和文献检索。

5. 写作与研究：辅助内容创作，如文章提取（article-extractor）、带引文的研究写作（content-research-writer）和脑暴工具。
 
6. 学习与知识管理：如 tapestry，用于构建知识网络。

7. 媒体与内容：处理多媒体，例如 YouTube 转录摘要（youtube-transcript）和图像增强（image-enhancer）。

8. 协作与项目管理：自动化 Git 推送（git-pushing）、会议洞察分析（meeting-insights-analyzer）和任务跟踪（linear-cli-skill）。

9. 安全与 Web 测试：漏洞扫描集成，如 FFUF 模糊测试（ffuf_claude_skill）和防御深度分析。

10. 实用与自动化：文件整理（file-organizer）和技能模板生成（skill-creator）。

开源项目
https://t.co/QZM0w1E5tn

![](https://pbs.twimg.com/media/G7SWtEKbYAANlql.jpg)
---

---
url: "https://x.com/shao__meng/status/1981900999033078086"
requested_url: "https://x.com/shao__meng/status/1981900999033078086?t=p_Tk7rMgIoKboOCpIRomfQ&s=09"
author: "meng shao (@shao__meng)"
author_name: "meng shao"
author_username: "shao__meng"
author_url: "https://x.com/shao__meng"
tweet_count: 1
---

## 1
https://x.com/shao__meng/status/1981900999033078086

[开源学习] Claude Excel Agent: Claude Agent SDK +  Skills 实现 Excel 数据交互，Skills 的引入使产品更具模块化和自主性：开发者可以将 Excel 操作封装为独立的 Skills，让 Claude 智能体根据用户查询自主触发，而非手动注册工具，作者 @trq212 

Skills 在 Claude Agent SDK 中的核心概念
Skills 是 Claude 的专属能力扩展，定义为文件系统中的 SKILL. md 文件（包含 YAML 前置元数据和 Markdown 说明），用于描述技能的触发条件（如“处理 Excel 数据”）。不同于可编程注册的工具，Skills 是自主发现的：Claude 根据技能的 description 字段判断是否调用，支持多文件资源和工具限制。 关键益处包括：
· 模块化：技能可复用，隔离复杂工作流（如 Excel 读取+分析）。
· 自主性：Claude 在多轮对话中动态调用，无需显式指令。
· 集成：Skills 与 SDK 工具（如 Read、Bash）结合，扩展智能体行为。

在这个开源项目中，Skills 可将原有工具（如 excel_tool.py 中的 read_excel）转化为独立技能，提升从原型到生产级的可扩展性。

项目中 Using Skills 的实施步骤
官方文档强调 Skills 的使用需通过 SDK 配置加载和启用，以下步骤直接适用于 excel-demo 项目（基于 Python SDK）：

1. 定义 Skills 文件：
   · 在项目根目录创建 .claude/skills/excel-processor/ 子目录。
   · 添加 SKILL. md 文件，将原有 excel_tool.py 的功能封装为技能，支持资源如自定义脚本。

2. 配置 SDK 选项：
   修改 main. py 中的 ClaudeAgentOptions，启用 Skills 加载：这允许 Claude 自动发现并调用 Excel 技能，而非仅依赖 @ tool 装饰器。

3. 初始化与查询：
   在入口脚本中，使用 query 函数处理输入：Claude 会匹配提示与技能描述，自主调用工具链（如读取 Excel → Pandas 分析）。

4. 测试与扩展：
   · 运行 python main. py，输入如“过滤销售额 > 10,000 的行”——Skills 确保上下文保留，支持迭代（如后续“生成图表描述”）。
   · 扩展：添加子技能目录，支持多 Excel 工作表或集成可视化工具。

项目与 Skills 的实际集成示例
在 excel-demo 中，原有工作流（加载 Excel → 工具调用 → 响应）可无缝升级为 Skills 驱动：
· 触发示例：用户查询“总结 Excel 销售数据” → Claude 检测 description 匹配 → 调用技能 → 使用 Pandas 输出“Q1 总销售额：$50,000，增长 15%”。
· 工具协同：Skills 可限制 allowed_tools 为项目特定（如仅 Read 和自定义 Excel 函数），避免全局工具滥用。
· 局限扩展：文档提及 Skills 适用于数据处理工作流（如 PDF 提取），类似地，此项目可演变为 Excel 专用技能库，支持大型文件或公式解析（需结合 openpyxl）。

开源地址：
https://t.co/slKw3S5XwO

> Author: Thariq (@trq212)
> URL: https://x.com/trq212/status/1981455233369907597
>
> Using Skills with the Claude Agent SDK
>
> How do you use skills to build agents? Here's an example demo I've built using one of our premade skills to make an excel demo agent.

![](https://pbs.twimg.com/media/G4EgWuMWcAAYt_b.jpg)
---

---
url: "https://x.com/shao__meng/status/1980641311549190651"
requested_url: "https://x.com/shao__meng/status/1980641311549190651?t=4YefukwdsTaaoMC7NuBuwA&s=09"
author: "meng shao (@shao__meng)"
author_name: "meng shao"
author_username: "shao__meng"
author_url: "https://x.com/shao__meng"
tweet_count: 1
---

## 1
https://x.com/shao__meng/status/1980641311549190651

[开源推荐] Anthropic 开源了最新发布的 Claude Skills，有 14 个示例直接复制来用，创意设计、开发构建、文档处理和企业沟通都有。

先复习一下 Skills 的概念
Skills (技能) 包含指令、脚本和资源的文件夹，Claude 可以动态加载这些内容，以提高在专业任务上的表现。简单来说，Skills 就是教会 Claude 以可重复的方式完成特定任务的"教程包"。

开源项目目的
· 示例展示 - 展示技能系统的各种可能性
· 学习参考 - 为开发者提供创建自定义技能的灵感和模式
· 技术规范 - 提供标准的技能格式定义

Skills 分类
项目包含 14 个示例技能，分为以下几类：

创意设计类
· algorithmic-art：使用 p5.js 创建生成艺术
· canvas-design：设计视觉艺术（PNG/PDF 格式）
· slack-gif-creator：创建适合 Slack 的动画 GIF

开发构建类
· artifacts-builder：构建复杂的 HTML artifacts
· mcp-server：创建 MCP 服务器集成外部 API
· webapp-testing：使用 Playwright 测试 Web 应用

企业沟通类
· brand-guidelines：应用品牌规范
· internal-comms：撰写内部沟通文档
· theme-factory：为 artifacts 应用专业主题

文档处理类
· docx、pdf、pptx、xlsx：处理各类办公文档

技术架构
技能的结构非常简洁：
· 每个技能就是一个文件夹
· 必须包含一个 SKILL. md 文件
· 文件包含 YAML 前置数据（元数据）和 Markdown 内容（具体指令）

工作原理
· 用户通过自然语言提及技能名称
· Claude 在技能注册表中查找匹配
· 加载对应的 SKILL. md 文件
· 按照文件中的指令执行任务

开源地址：
https://t.co/I9PkD8H203

![](https://pbs.twimg.com/media/G3ymvB0WsAAdLR2.jpg)
---

---
url: "https://x.com/shao__meng/status/1980953315514187833"
requested_url: "https://x.com/shao__meng/status/1980953315514187833?t=4YefukwdsTaaoMC7NuBuwA&s=09"
author: "meng shao (@shao__meng)"
author_name: "meng shao"
author_username: "shao__meng"
author_url: "https://x.com/shao__meng"
tweet_count: 1
---

## 1
https://x.com/shao__meng/status/1980953315514187833

Google 推出新一代学习平台：Google Skills，专注于帮助开发者和技术人员掌握 AI 和云计算技能。这是一个实践导向的学习平台，结合了 Google 十多年的 AI 创新经验。

核心特点

1. 实践为先的学习方式
· 强调动手操作 (hands-on learning) 而非纯理论学习
· 数据显示：有讲师指导的学习完成率达 90%，而自学完成率不到 5%
· 77% 的学习者更倾向于有讲师指导的培训

2. 三级认证体系
· 证书(Certificates)：入门级，无需前置条件，完成学习路径即可获得可分享的数字凭证，适合职业转型
· 技能徽章(Skill Badges)：中级，通过完成系列课程证明实际技术能力，可向公司展示
· 认证(Certifications)：专业级，需通过监考考试，获得 Google Cloud 行业认可的专业认证

3. 社区驱动学习
· 可加入 Google Cloud Innovators 计划
· 每月获得 35 个免费学习积分用于实践练习

价值主张
· 企业价值：投资动手学习的公司，员工留存率提升 133%
· 个人价值：在 AI 时代"为未来技能做准备"(future proof)，而不是被动应对
· 可信度：依托 Google 在云计算和 AI 领域的技术积累

在线学习地址
https://t.co/vEAw5qwlDi

![](https://pbs.twimg.com/media/G33CDVyXgAA7KYj.jpg)
---

---
url: "https://x.com/ShenzhiWang_THU/status/1808322635782410584"
requested_url: "https://x.com/ShenzhiWang_THU/status/1808322635782410584"
author: "Shenzhi Wang🌟 (@ShenzhiWang_THU)"
author_name: "Shenzhi Wang🌟"
author_username: "ShenzhiWang_THU"
author_url: "https://x.com/ShenzhiWang_THU"
tweet_count: 6
---

## 1
https://x.com/ShenzhiWang_THU/status/1808322635782410584

🔥 After the 9B model, we present Gemma-2-27B-Chinese-Chat: the 1st Gemma2 27B model optimized for Chinese&amp;English, finetuned on &gt;100K preference pairs!

🚀 Our model excels in Chinese, with improved logic, coding, math, and writing skills.

More info:🧵⬇️
https://t.co/YPjGqa7xbu

## 2
https://x.com/ShenzhiWang_THU/status/1808323085617320432

Various GGUF models for Gemma-2-27B-Chinese-Chat:
https://t.co/Q1qevpPKVI

## 3
https://x.com/ShenzhiWang_THU/status/1808323363410268438

The ollama model for Gemma-2-27B-Chinese-Chat:

https://t.co/mCsdSvA0KF

## 4
https://x.com/ShenzhiWang_THU/status/1808323817347207425

The fine-tuning algorithm we used is ORPO.

https://t.co/jUXJMFpEQ1

## 5
https://x.com/ShenzhiWang_THU/status/1808324641083347097

Our Gemma-2-9B-Chinese-Chat:
https://t.co/xNpec8Uhz4

> Author: Shenzhi Wang🌟 (@ShenzhiWang_THU)
> URL: https://x.com/ShenzhiWang_THU/status/1807640624402923779
>
> 🔥Introducing Gemma-2-9B-Chinese-Chat: the 1st Gemma-2 model tailored for Chinese&amp;English users, fine-tuned on &gt;100K preference pairs!
>
> 🚀Our model excels in Chinese prompts, and shows improved logic, coding, math, and writing skills.
>
> More info: 🧵⬇️
>
> https://t.co/r8Ho8DjMTT

## 6
https://x.com/ShenzhiWang_THU/status/1808376127045751013

We have included various examples generated by shenzhi-wang/Gemma-2-27B-Chinese-Chat, including examples of role playing, function calling, math, RuoZhiBa (弱智吧), safety, writing, and coding, etc.  Have a look on our huggingface repo😆

https://t.co/GdmBeIx4l8 https://t.co/b143OucV8Y

![](https://pbs.twimg.com/media/GRikRbpb0AQl94T.jpg)
---

---
url: "https://x.com/simonw/status/1973046547144380697"
requested_url: "https://x.com/simonw/status/1973046547144380697?t=1Zs88I9x8QACSwjsYfwllg&s=09"
author: "Simon Willison (@simonw)"
author_name: "Simon Willison"
author_username: "simonw"
author_url: "https://x.com/simonw"
tweet_count: 2
---

## 1
https://x.com/simonw/status/1973046547144380697

One of the new skills required to get the most out of AI-assisted coding tools - Claude Code, Codex CLI, etc - is designing agentic loops: carefully selecting tools to run in a loop to achieve a specified goal. Do this well and you can solve many coding problems with brute force.

## 2
https://x.com/simonw/status/1973046549597847714

Here's my expanded explanation of what it means to design an agentic loop, how to do it safely (while running in YOLO mode!) and the kinds of interesting problems this approach can be used to tackle https://t.co/sRIx4qWfz9
---

---
url: "https://x.com/Stephen4171127/status/1993244561179898193"
requested_url: "https://x.com/Stephen4171127/status/1993244561179898193?s=09"
author: "熊布朗 (@Stephen4171127)"
author_name: "熊布朗"
author_username: "Stephen4171127"
author_url: "https://x.com/Stephen4171127"
tweet_count: 1
---

## 1
https://x.com/Stephen4171127/status/1993244561179898193

强推 ! 收藏！ 想研究 Claude Skill，看这一篇文章就够了！作者写得太好了，写一篇好文章比做一个烂产品有用太多了。
https://t.co/edAAt0zApB https://t.co/M7IYxbDLcr

![](https://pbs.twimg.com/media/G6lsiW6XgAAQ7Dk.jpg)
---

---
url: "https://x.com/TheFigen_/status/1804659350675308611"
requested_url: "https://x.com/TheFigen_/status/1804659350675308611?s=09&t=EfKLg0yuJ5nv9XZ1EgZx6A"
author: "The Figen (@TheFigen_)"
author_name: "The Figen"
author_username: "TheFigen_"
author_url: "https://x.com/TheFigen_"
tweet_count: 1
---

## 1
https://x.com/TheFigen_/status/1804659350675308611

Skills https://t.co/jhpsEptvLC

![video](https://pbs.twimg.com/ext_tw_video_thumb/1804659257444372480/pu/img/qnjIwhTaN4DfTtqL.jpg)
[video](https://video.twimg.com/ext_tw_video/1804659257444372480/pu/vid/avc1/680x640/Zyo3vhdcCvFazCdC.mp4?tag=12)
---

---
url: "https://x.com/TheFigen_/status/1804659350675308611"
requested_url: "https://x.com/TheFigen_/status/1804659350675308611"
author: "The Figen (@TheFigen_)"
author_name: "The Figen"
author_username: "TheFigen_"
author_url: "https://x.com/TheFigen_"
tweet_count: 1
---

## 1
https://x.com/TheFigen_/status/1804659350675308611

Skills https://t.co/jhpsEptvLC

![video](https://pbs.twimg.com/ext_tw_video_thumb/1804659257444372480/pu/img/qnjIwhTaN4DfTtqL.jpg)
[video](https://video.twimg.com/ext_tw_video/1804659257444372480/pu/vid/avc1/680x640/Zyo3vhdcCvFazCdC.mp4?tag=12)
---

---
url: "https://x.com/thisguyknowsai/status/1956269176391393699"
requested_url: "https://x.com/thisguyknowsai/status/1956269176391393699?t=4YmrFU6X6WY0T6XIu9qlDw&s=09"
author: "Brady Long (@thisguyknowsai)"
author_name: "Brady Long"
author_username: "thisguyknowsai"
author_url: "https://x.com/thisguyknowsai"
tweet_count: 28
---

## 1
https://x.com/thisguyknowsai/status/1956269176391393699

This might be the most underrated AI skill of 2025:

JSON prompting.

It turns your LLMs like ChatGPT, Gemini, and Claude into consistent, structured agents no hallucinations, no mess.

Here’s how it works (with copy-paste templates):

## 2
https://x.com/thisguyknowsai/status/1956269188634567025

first…what is json prompt writing?

it's just putting your prompt inside a structured format.
like this:

{
  "task": "summarize this article",
  "audience": "college students",
  "length": "100 words",
  "tone": "curious"
}

not english.
not vibes.
just instructions, like a form

## 3
https://x.com/thisguyknowsai/status/1956269200668025080

why does it work so well?

llms don’t "understand" language the way we do.
they follow patterns and structure.
and json is ultra-structured.
it leaves no ambiguity.

they don’t have to guess what you mean.
you’re telling them exactly what you want.

## 4
https://x.com/thisguyknowsai/status/1956269220045738179

think of it like this:

regular prompt:

can you write a tweet about dopamine detox?

json-style:

{
  "task": "write a tweet",
  "topic": "dopamine detox",
  "style": "viral",
  "length": "under 280 characters"
}

see the difference?
clear. modular. machine-readable. https://t.co/OVXu60zpIb

![](https://pbs.twimg.com/media/GyYQfRla0AAcXy9.png)

## 5
https://x.com/thisguyknowsai/status/1956269235841458281

want even sharper outputs?

you can nest the json.

{
  "task": "write a thread",
  "platform": "twitter",
  "structure": {
    "hook": "strong, short, curiosity-driven",
    "body": "3 core insights with examples",
    "cta": "ask a question to spark replies"
  },
  "topic": "founder productivity systems"
}

you just turned prompt spaghetti into clean code.

![](https://pbs.twimg.com/media/GyYQgNOa4AQaBVY.jpg)

## 6
https://x.com/thisguyknowsai/status/1956269248348873069

so how do you write json prompts?

3 basic rules:

- use key-value pairs
- be explicit
- use nested objects for structure

example:

{
  "task": "generate a list",
  "topic": "books that improve thinking",
  "audience": "young entrepreneurs",
  "output_format": "markdown bullets"

}

## 7
https://x.com/thisguyknowsai/status/1956269260227129853

this works across all major models.

chatgpt? yes.
claude? thrives on it.
gemini? understands structure well.
mistral, gpt-4o, etc? all love structured input.

some even prefer it.

## 8
https://x.com/thisguyknowsai/status/1956269277620949282

a quick comparison to prove it:

normal prompt:

recommend books that help me think clearer

json prompt:

{
  "task": "recommend books",
  "topic": "thinking clearly",
  "audience": "entrepreneurs",
  "output_format": "list of 5 with one-sentence summaries"
}

run both.
the second is crisper, clearer, and more relevant.

![](https://pbs.twimg.com/media/GyYQilpa4AAhuK-.jpg)

## 9
https://x.com/thisguyknowsai/status/1956269341605028330

here's one you can try in Veo 3 right now:

simple prompt:

show me a product demo style video of a fitness app https://t.co/tJiCXkUnaL

![video](https://pbs.twimg.com/amplify_video_thumb/1956269291076247558/img/GbtzHoxxz7a9zYus.jpg)
[video](https://video.twimg.com/amplify_video/1956269291076247558/vid/avc1/1280x720/TOUVUSI3myfBmbe7.mp4?tag=14)

## 10
https://x.com/thisguyknowsai/status/1956269405564031220

json version:

{
  "task": "generate a video",
  "video_type": "product demo",
  "theme": "fitness app",
  "duration": "8 seconds",
  "tone": "energetic and sleek",
  "visual_style": "clean UI, fast transitions"
}

watch how much better the output and exact. https://t.co/MD6PRz5FRq

![video](https://pbs.twimg.com/amplify_video_thumb/1956269354909323264/img/sRrSI-f_2yxujPj-.jpg)
[video](https://video.twimg.com/amplify_video/1956269354909323264/vid/avc1/1280x720/b22TFb2im2V42lf4.mp4?tag=14)

## 11
https://x.com/thisguyknowsai/status/1956269417635233963

why this works:

models like gpt are trained on code, docs, apis, and structured data.
json looks like the stuff they were fed.
so they treat it as higher-signal.

the less they have to guess, the better the result.

## 12
https://x.com/thisguyknowsai/status/1956269429542805650

another example:

bad prompt:

write me a cold email that converts

better (json):

{
  "task": "write cold email",
  "audience": "SaaS founders",
  "product": "ai sales automation tool",
  "goal": "book a 15-minute call",
  "tone": "friendly but confident"
}

gets straight to the point.
every word earns its place.

## 13
https://x.com/thisguyknowsai/status/1956269441404248285

bonus: you can even write inside the json

like this:

{
  "task": "improve writing",
  "input": "Our team is proud to announce the next chapter of our journey.",
  "goal": "make it more vivid and emotional",
  "audience": "customers",
  "tone": "authentic and inspiring"
}

clean. surgical. upgradeable.

## 14
https://x.com/thisguyknowsai/status/1956269453320315050

want to write content that always hits?

use this json skeleton:

{
  "task": "write content",
  "platform": "twitter",
  "structure": {
    "hook": "short, punchy, curiosity-driven",
    "point": "3-5 insights, each 2-3 sentences",
    "action": "one question to spark replies"
  },
  "topic": "your topic here",
  "tone": "casual and smart"
}

it works for almost anything.

## 15
https://x.com/thisguyknowsai/status/1956269465232191785

here are 5 high-leverage use cases people use AI for daily — with json templates:

you can copy/paste these and just swap out the input.
plug-and-play style.

## 16
https://x.com/thisguyknowsai/status/1956269477123047656

1. generate videos with voice (e.g. Veo 3)

{
  "task": "generate video",
  "platform": "Veo",
  "video_type": "explainer",
  "topic": "how to start a dropshipping store",
  "duration": "60 seconds",
  "voiceover": {
    "style": "calm and confident",
    "accent": "US English"
  },
  "visual_style": "modern, clean, fast cuts"
}

## 17
https://x.com/thisguyknowsai/status/1956269489190002783

2. generate content (for social, blogs, emails, etc)

{
  "task": "write content",
  "platform": "twitter",
  "structure": {
    "hook": "short, curiosity-driven",
    "body": "3 insights with smooth flow",
    "action": "1 strong question"
  },
  "topic": "how to stay focused as a solo founder",
  "tone": "relatable and smart"
}

## 18
https://x.com/thisguyknowsai/status/1956269500938248446

3. write or debug code

{
  "task": "write code",
  "language": "python",
  "goal": "build a script that renames all files in a folder",
  "constraints": ["must work on MacOS", "include comments"],
  "output_format": "code only, no explanation"
}

## 19
https://x.com/thisguyknowsai/status/1956269512753598620

4. turn raw ideas into a business/brand strategy

{
  "task": "act as brand consultant",
  "client": "early-stage AI tool",
  "goal": "define clear positioning",
  "deliverables": ["1-liner", "target audience", "3 key differentiators"],
  "tone": "simple and strategic"
}

## 20
https://x.com/thisguyknowsai/status/1956269524606706097

5. turn information into consulting deliverables

{
  "task": "create consulting doc",
  "input": "paste research or notes here",
  "client": "retail ecommerce brand",
  "deliverables": ["SWOT analysis", "growth roadmap", "3 quick wins"],
  "output_format": "markdown",
  "tone": "sharp and practical"
}

## 21
https://x.com/thisguyknowsai/status/1956269536371695923

big tip:

json makes prompt chaining easier.
you can pass outputs as inputs to the next task.
llms understand the “steps” like an api.
each step has a key, each value is an instruction.

## 22
https://x.com/thisguyknowsai/status/1956269548128362787

when you don’t want json?

if your goal is creativity, chaos, or surprise.
like dream journaling.
storytelling for kids.
or idea generation without constraints.

json = structure
freeform = chaos

choose based on outcome.

## 23
https://x.com/thisguyknowsai/status/1956269559905968393

json works because it speaks machine language
but it also helps you think clearly.

you define the goal, structure, audience, format upfront.
no back-and-forth.
no 5 tries to get it right.

## 24
https://x.com/thisguyknowsai/status/1956269571675185413

he shift is this:

stop “asking” the ai for stuff.
start specifying exactly what you want.
like a builder giving a blueprint.
not a poet throwing vibes.

## 25
https://x.com/thisguyknowsai/status/1956269583419236611

remember:

- json is just structured prompting
- it gives clarity to both you and the model
- it works across tools, models, and formats
- it makes you think like an architect
- and it’s shockingly easy to learn

## 26
https://x.com/thisguyknowsai/status/1956269595138121897

everyone talks about "prompt engineering"
but 90% of results come from
clear structure

+

precise intent

json gives you both.

## 27
https://x.com/thisguyknowsai/status/1956269606903144859

AI is not going to take your job.

Instead, it's going to make you rich and help you build businesses online.

You need to know the best tools, and that's all.

We can help you find the best business AI tools.

Check our tools directory today:

https://t.co/897zpbR3sy

## 28
https://x.com/thisguyknowsai/status/1956269618835939464

Looking for more posts like this?

Follow me @thisguyknowsai and you'll get 1x post every single day.

And don't forget to repost the thread to reach more.

Thanks for checking!

> Author: Brady Long (@thisguyknowsai)
> URL: https://x.com/thisguyknowsai/status/1956269176391393699
>
> This might be the most underrated AI skill of 2025:
>
> JSON prompting.
>
> It turns your LLMs like ChatGPT, Gemini, and Claude into consistent, structured agents no hallucinations, no mess.
>
> Here’s how it works (with copy-paste templates):
---

---
url: "https://x.com/vista8/status/2015445379769356678"
requested_url: "https://x.com/vista8/status/2015445379769356678"
author: "向阳乔木 (@vista8)"
author_name: "向阳乔木"
author_username: "vista8"
author_url: "https://x.com/vista8"
tweet_count: 2
---

## 1
https://x.com/vista8/status/2015445379769356678

根据群友需求，缝合了一个万能NotebookLM 解读 Skill

无论微信链接，还是Epub、Word/PPT/PDF。

甚至图片、音频都可以自动传到NotebookLM。

生成PPT、思维导图、播客、信息图等支持的格式。

用到工具有Notebooklm-py、微信文章读取MCP、微软的格式转换Markitdown等。

Github在评论区

![](https://pbs.twimg.com/media/G_hMl0bX0AAGVaZ.jpg)

## 2
https://x.com/vista8/status/2015445427190186079

Github地址：https://t.co/WwMvXeqUhR
---

---
url: "https://x.com/vista8/status/2008714622035956104"
requested_url: "https://x.com/vista8/status/2008714622035956104"
author: "向阳乔木 (@vista8)"
author_name: "向阳乔木"
author_username: "vista8"
author_url: "https://x.com/vista8"
tweet_count: 1
---

## 1
https://x.com/vista8/status/2008714622035956104

Obsidian CEO写的Skill，基于X用户调研。

这几天，他好像经常问大家用给Ob写了什么好玩的Claude Skill。

其实，大家的回复更精彩，但他写的很基础底层。

① 写出Obsidian风格的Markdown （内链、属性等）
② 生成.Base 文件的过滤器和公式
③ 生成Canva无限画布等

用这个很简单，只需要告诉Claude Code：

安装这里的skills  https://t.co/QlNfzOHoDR

> Author: kepano (@kepano)
> URL: https://x.com/kepano/status/2008576058715787729
>
> are there any Claude Skills you have found useful in your Obsidian vault?

![](https://pbs.twimg.com/media/G-BiB8laMAA4Lx2.jpg)
---

---
url: "https://x.com/vista8/status/1990686959224959330"
requested_url: "https://x.com/vista8/status/1990686959224959330"
author: "向阳乔木 (@vista8)"
author_name: "向阳乔木"
author_username: "vista8"
author_url: "https://x.com/vista8"
tweet_count: 1
---

## 1
https://x.com/vista8/status/1990686959224959330

第二个Skill做好了。

生成文章后，让 @oran_ge 家的Listenhub念出来。

学习知识越来越方便了。

下一步研究，怎么把音频自动变成视频。 https://t.co/l91dkeOrEk

> Author: 向阳乔木 (@vista8)
> URL: https://x.com/vista8/status/1990668495496098194
>
> 一直觉得Claude Skill这个概念难懂，也不知道怎么开始
>
> 经过昨天研究，发现我想复杂了。
>
> 上手其实很简单，如果你有Claude Code，无论官方还是中转。（ 比如我用的兔子API @tuzi_ai  的中转）
>
> 一共三步：
>
> 1. 运行Claude Code，输入/plugin , 选择add marketplace，输入下面网址回车
> https://t.co/dw9V8P7qjY
>
> 2. 这时会看到两个安装选项，一个是document-skill，一个是example-skill，都装上。
>
> 第一个用于处理pdf、word等文档，第二个是样例，未来也能调用。
>
> 3. 跟 Claude 对话说：“一步步引导我写第一个Claude skill”
>
> Claude会抱怨需求不清楚，让你回答问题，明确需求。
>
> 我回答：我想要一个写作Skill，能联网，会用我的提示词，并且安装一个seedream MCP用于生成配图插入文章。
>
> Claude会追问细节，给你一些选择题，都答完，需求明确后。
>
> 它会创建一系列文件夹和文件。
>
> 第一个写作Skill就做好了！

![](https://pbs.twimg.com/media/G6BW_YvbMAktFFo.jpg)
![](https://pbs.twimg.com/media/G6BXOEhbMAEoKYW.jpg)
---

---
url: "https://x.com/vista8/status/1990668495496098194"
requested_url: "https://x.com/vista8/status/1990668495496098194"
author: "向阳乔木 (@vista8)"
author_name: "向阳乔木"
author_username: "vista8"
author_url: "https://x.com/vista8"
tweet_count: 1
---

## 1
https://x.com/vista8/status/1990668495496098194

一直觉得Claude Skill这个概念难懂，也不知道怎么开始

经过昨天研究，发现我想复杂了。

上手其实很简单，如果你有Claude Code，无论官方还是中转。（ 比如我用的兔子API @tuzi_ai  的中转）

一共三步：

1. 运行Claude Code，输入/plugin , 选择add marketplace，输入下面网址回车 
https://t.co/dw9V8P7qjY

2. 这时会看到两个安装选项，一个是document-skill，一个是example-skill，都装上。

第一个用于处理pdf、word等文档，第二个是样例，未来也能调用。

3. 跟 Claude 对话说：“一步步引导我写第一个Claude skill”

Claude会抱怨需求不清楚，让你回答问题，明确需求。

我回答：我想要一个写作Skill，能联网，会用我的提示词，并且安装一个seedream MCP用于生成配图插入文章。

Claude会追问细节，给你一些选择题，都答完，需求明确后。

它会创建一系列文件夹和文件。

第一个写作Skill就做好了！

![](https://pbs.twimg.com/media/G6BD1U-boAAHlAP.jpg)
![](https://pbs.twimg.com/media/G6BEPTMbYAASSPD.jpg)
![](https://pbs.twimg.com/media/G6BFMoibMAEUSNJ.jpg)
![](https://pbs.twimg.com/media/G6BFmjWbUAAzmIr.jpg)
---

---
url: "https://x.com/wangyuanzju/status/1979539828082626593"
requested_url: "https://x.com/wangyuanzju/status/1979539828082626593?t=u6zZfibby-igIeWC42mHQA&s=09"
author: "WY (@wangyuanzju)"
author_name: "WY"
author_username: "wangyuanzju"
author_url: "https://x.com/wangyuanzju"
tweet_count: 1
---

## 1
https://x.com/wangyuanzju/status/1979539828082626593

Claude Skills可能走对路了

前天Anthropic发布了Claude Skills，这是一种让AI获取新能力的全新机制。很不错的设计，包含了软件两个最主要的组成部分：程序和资源，还没有什么别的复杂性。架构看起来很合理，虽然要实际用用才能感觉出来是不是真的好用，但初步从架构设计看，感觉Claude Skills在方向上可能走对路了，整个AI行业可能走对路了。

简洁的力量：程序+资源就够了

Skills的核心概念非常简单：一个Skill就是一个文件夹，包含指令、脚本与资源。具体来说，每个Skill包含三样东西：指令(Instructions)告诉Claude该做什么、脚本(Scripts)执行具体任务、资源(Resources)提供模板和辅助内容。因为自然语言也是代码，指令和脚本其实是分不清的，都属于程序。

这种设计的合理之处在于它抓住了软件的本质。软件不就是程序和资源吗？程序负责逻辑，资源负责数据和素材。Skills把这两者有机结合，又没有引入什么别的复杂性。

更重要的是Skills的按需加载机制。Claude只会在Skill与当前任务相关时才会调用，并且采用渐进式披露：先加载元数据(约100词)，再加载https://t.co/8CjlRMvOgF主体(也比较小)，最后才是具体的资源文件。这种设计既高效又节省token，体现了对成本和性能的深度考量。

AI能力扩展的演进：从Plugin到Skills

要理解Skills的价值，需要回顾OpenAI和Anthropic在AI能力扩展上的探索历程。

OpenAI的Plugin是第一次尝试，但看起来是不成功的尝试。Plugin主要依赖API调用，虽然概念不错，但实际体验并不理想，很快就被弱化了。后来推出的GPTs允许用户定制AI的知识和行为，但本质上仍然是基于提示词工程的定制，缺乏真正的能力扩展。

最新的Apps则希望把第三方的界面直接嵌进来，感觉步子迈得有点大。让AI直接操作第三方应用的界面，这种computer use式的方案虽然听起来很酷，但实际可控性和可靠性都面临巨大挑战，而且第三方应用也不愿意被嵌入的这么深。百度很多年前想做框计算，目的是类似的，并没有成功。

Anthropic自己推出的MCP(Model Context Protocol)走的是另一条路，主要通过API调用已有服务的能力，和Skills的定位不同。MCP更多是为了连接外部系统和服务，而Skills则是为Claude赋予新的原生能力。

相比之下，Skills找到了一个更优雅的平衡点。它用Markdown这种人人都能理解的格式来描述能力，可以包含详细的使用说明和示例。开发者创建一个Skill，就像是"给Claude写一份入职手册"。而且Skills可以打包分享，形成开放的生态系统，这大大降低了开发门槛。

Anthropic一口气开源了20多个Skills，涵盖创意设计、开发技术、企业应用等各个领域。这种开放的姿态，很可能会推动一个繁荣的Skills生态的形成。资源的例子很好理解：Canvas-fonts包含很多字体文件，这样Claude在生成设计时就能直接调用。

仍需改进的地方

当然，任何新技术都不可能完美。Skills目前也存在一些明显的不足。

首先是技术门槛问题。虽然Skills用Markdown编写降低了理解难度，但官方的一些Skills仍然依赖于apt-get这样不够亲民的指令，至少对大多数Windows的用户这一步就直接挂了。普通用户希望的是一个软件包一装就灵，而不是还要装一大堆依赖。如何让Skills的创建和使用更加大众化，是Anthropic需要继续优化的方向。

其次，Skills看起来不容易拥有自己的存储和数据库。这在处理需要持久化状态的任务时可能会成为限制。比如，如果我想创建一个帮我跟踪工作进展的Skill，它需要记住之前的任务状态和历史数据，但现在的Skills架构似乎不太支持这种场景。不过或许可以在Skill里调用sqlite这样的数据库命令来实现这一点？

结语

Claude Skills的发布，为AI能力扩展提供了一个简洁而优雅的解决方案。相比OpenAI的Plugin、GPTs和Apps等尝试，以及Anthropic自己的MCP，Skills在易用性、可控性和生态开放性之间找到了更好的平衡。它避免了过度工程化的陷阱，用最小的复杂度实现了核心价值。

在AI原生应用的探索中，我们都在寻找那个平衡点：既要充分发挥AI的能力，又要保持用户体验的简洁流畅；既要提供强大的功能，又要避免不必要的复杂性。Skills在这个平衡上做出了有价值的尝试，值得我们这些AI产品从业者认真研究和借鉴。
---

---
url: "https://x.com/wquguru/status/1987321760036102450"
requested_url: "https://x.com/wquguru/status/1987321760036102450?t=Yqc-GZpgFIWxH0pulHAyBg&s=09"
author: "WquGuru🦀 (@wquguru)"
author_name: "WquGuru🦀"
author_username: "wquguru"
author_url: "https://x.com/wquguru"
tweet_count: 1
---

## 1
https://x.com/wquguru/status/1987321760036102450

Claude Code Skill + Claude Commands帮助我将特定任务的效率提升了50%以上

传统上，对接一个新的cex或者dex，任务调研、方案编写、技术实现是割裂的，即使各自都能或多或少用到AI，但整体来说AI提效并没有达到质的飞跃

Claude Code Skill出来后，将这个复杂任务AI工作流化，拆解为单步可验证的skill或者command：

- 任务调研skill：核心是几个从官方文档、Github仓库抓取信息的脚本，最终输出一份Markdown文档

- 接口调研skill：研究鉴权和接口问题，输出json文件

- 代码实现command：通过prompt引导大模型，基于上述json文件和markdown，逐步实现核心代码和单元测试

刷新一下现在的认知：重复一遍以上的任务，能AI化的一切AI化（写skill本身任务也可做成skill）

> Author: AlexZ 🦀 (@blackanger)
> URL: https://x.com/blackanger/status/1987201629301641624
>
> claude code skill 是真的好用 ，丝滑
---

---
url: "https://x.com/xiaoerzhan/status/2007066473811054859"
requested_url: "https://x.com/xiaoerzhan/status/2007066473811054859"
author: "小耳👂Jane｜Xiaoer (@xiaoerzhan)"
author_name: "小耳👂Jane｜Xiaoer"
author_username: "xiaoerzhan"
author_url: "https://x.com/xiaoerzhan"
tweet_count: 3
---

## 1
https://x.com/xiaoerzhan/status/2007066473811054859

关于最近很火的skills，我拔啦到以下资源，请诸位收藏，可以来个资源大库：

下面这些，基本都是 star 500+、更新还算勤快的 Skills 仓库，可以直接当素材库撸：
1. https://t.co/J86EmnBDp1
2. https://t.co/zTFPg1gDDz
3. https://t.co/PaL7HL0IgI
4. https://t.co/z0VjiOg9q4
5. https://t.co/g3ZyLChUAx
6. https://t.co/ZgYDvPwR95
7. https://t.co/SalqYp4VFr
8. https://t.co/yNhqJWa19k
9. https://t.co/cxLuvpj7o9
10. https://t.co/zmCSRsE2kg
11. https://t.co/QHyo8opYft

这些加起来，差不多能把当下主流 Skill 场景扫一遍：
文档清洗、EPUB 转换、Markdown 处理。

AWS CDK、D3 可视化、iOS 模拟器这类"重型活"。

CSV 智能分析、根因追溯、竞品广告分析、域名脑暴。

会议洞察、内容研究、视频下载、GIF 生成、发票整理、文件归档、代码审查。
还有安全相关的威胁猎杀、数字取证。
如果你是开发，可以直接锁定两个仓库起步：
• 官方：anthropics/skills
https://t.co/Tc0WvAPwcf
• 江湖：obra/superpowers
https://t.co/J86EmnBDp1

内容创作者就去翻 ComposioHQ 的精选 Skills：
https://t.co/zTFPg1gDDz

里面像 Content Research Writer、Theme Factory 这类，都是可以直接嵌进你日常内容生产流程的。

数据分析师也可以盯着 ComposioHQ：
CSV Data Summarizer、Meeting Insights，一边跑表、一边总结会议，省掉一大堆低价值操作。

设计相关的，就老老实实抄官方的 Canvas Design、Brand Guidelines，在 anthropics/skills 里都能看到。

把自己的品牌规则固化成 Skill，让 AI 自己帮你守规矩，而不是靠设计师一条条盯。

## 2
https://x.com/xiaoerzhan/status/2007603162228896046

原文链接在这里：https://t.co/v4UuvNkZl2…

## 3
https://x.com/xiaoerzhan/status/2007636789327286524

加到一起来:

现在已经有一批现成的 Skills 聚合站，把全网高手的成果都摆在你面前，内容多、更新快、还有分类和搜索：

• https://t.co/tGS9VBIg3r• https://t.co/kHWQ2b0JNq• https://t.co/kZ5iHTPcol
• https://t.co/tGS9VBIg3r • https://t.co/kHWQ2b0JNq • https://t.co/kZ5iHTPcol

你只要刷一圈，就会发现：真正好用的 Skill，都不是"堆功能"，而是把一个具体场景打磨到极致。

官方 Skills

如果只挑一个仓库去精读，那一定是 Anthropic 官方的： https://t.co/Tc0WvAPwcf…

它不是那种"随便丢几个 demo 应付下社区"的项目，而是把 Claude 线上真正在跑的生产级能力，原封不动摊开给你看： 文档处理四大件：Word / PDF / PPT / Excel，从创建、编辑到分析，流程写得极细，提示词、参数、边界都清清楚楚。

开发者工具：MCP 服务器、Web 应用测试、Artifacts 构建，一看就是为真实工程环境设计的。

创意设计：算法艺术、Canvas 设计、主题工厂，不是玩票，是能直接拿去跑活的方案。

更关键的是，你在 https://t.co/3aAaYssIbc 里点的那些"文档创建""智能分析"，背后就是这些 Skill。

也就是说，这个库本质是"官方拆解自家产品的内部能力模型"。

安装也很简单，要么从官方插件市场点一点，要么直接用命令挂上去：

/plugin marketplace add anthropics/skills /plugin install document-skills@anthropic-agent-skills
/插件市场 添加人类画/技能 /plugin install document-skills@anthropic-agent-skills
---

---
url: "https://x.com/xiaokedada/status/1981326177836159224"
requested_url: "https://x.com/xiaokedada/status/1981326177836159224?t=nYEQiTyvANPcRwGmRkZ_lg&s=09"
author: "nazha (@xiaokedada)"
author_name: "nazha"
author_username: "xiaokedada"
author_url: "https://x.com/xiaokedada"
tweet_count: 1
---

## 1
https://x.com/xiaokedada/status/1981326177836159224

#分享 大脑和工具之间的抽象：Skills

Anthropic 前几天推出 Skills，今天研究了下，第一眼就让我感觉怎么跟 Cursor Rules 的设计一模一样：标题、描述和被“卸载”到文件系统的详细内容。

接着仔细看了 Anthropic 提供的 Skills 示例https://t.co/Idg6aRw6zs，强烈觉得这恐怕又是 Anthropic 公司内部 dogfooding 的结果。

我的理解是：Skills 描述的对人类技能的抽象。

## MCP 和 Skills

一般，我们把 MCP 定义为 Agent 的 **工具能力**，能够访问外部系统、执行相关流程和获取关键信息。当然，MCP 也可以来做跟 Skills 相关的事情，它可以很狭义，也可以很广义，这主要看在具体实践中的定义。

技能是更高纬度的，通过学习、训练或工作经验获得的能力。之前主要是依赖 LLMs 的内在的通用能力，而 Skills 有点类似于强化学习路径，让 LLM 有一个可参考的模板。

简单理解，MCP 不能跟 Skills 混为一谈：MCP 定位在工具，Skills 定位在技能。

在 Anthropic 发布的这张图也并没有表达 Skills 替换 MCP 的意思，工具应该是更原子化的东西。而工具 = MCP + 命令行 + 自定义脚本 + ...

## Skills 是 Anthropic 让 Claude Code/Claude Web 向迈向通用 Agent 做的努力

Anthropic 在 Claude Code 中也集成了 Skills，显然是看到了 Claude Code 在通用 Agent 方向的潜力，而不仅仅是写代码（拜托，先换个名字，不要叫 Claude Code 了）。

## 再来看 Skills 的设计

第一个感觉就是对普通人来说真的简单。你要实现一个 MCP 工具，非编程科班出身的还真有点难度，理解 MCP 的各个概念就能让人退而却步。而 Skill 的设计呢，无非就是写文档、讲明白事情就可以。

为了实现在 Skills 执行脚本和代码，Anthropic 就必须提供一个虚拟执行环境，将部分困难转交给容器执行环境（这也许是下一个技术热点）。当然，并不是批评 MCP，MCP在设计的时候，也许并没有这个共识存在。

## 给我们在设计 Agent 架构时的启发

技能的部分，在之前的架构设计中，有一部分是会演变成子智能体，技能详情变成了子智能体的系统提示，即 Agent as Tool / Agent as Skill 的设计。若在智能体和工具之间又加了一个技能层，给我们在设计 Agent 架构的时候，就要思考得更多了，第一个问题就是是否需要额外引入一个 Agent，如果这个 Agent 的能力能够被 Skill 承载？

对于多智能体的架构，目前我看到的一些产品，比如 Manus、 Claude Code 都是很谨慎的。Skills 给我们在设计 Agent 的时候提供另一条思路：有技能的智能体。

## 了解 Skill, 我的建议

先从 https://t.co/Idg6aRw6zs 的每个例子开始，对技能是什么有个初步的概念。再看下 https://t.co/QAr6wTCjMT 这篇工程文章，深入了解 Skills 的设计。

最后，我表示我很喜欢 Skill。哪怕 Cursor Rules 出来很久，这也是我也没取思考过的工程设计。也许像浩瀚天空的一颗星，指明了一些方向。

![](https://pbs.twimg.com/media/G38UeVVWQAALpX8.jpg)
![](https://pbs.twimg.com/media/G38U6YbXIAAtXH2.jpg)
---

---
url: "https://x.com/yan5xu/status/1989171335818600488"
requested_url: "https://x.com/yan5xu/status/1989171335818600488?t=Qrji2R93pOl8d-Rp6nqVTg&s=09"
author: "yan5xu (@yan5xu)"
author_name: "yan5xu"
author_username: "yan5xu"
author_url: "https://x.com/yan5xu"
tweet_count: 2
---

## 1
https://x.com/yan5xu/status/1989171335818600488

claude skills 有个没怎么被看到的点，就是信息分层设计。首先用元信息替代完整信息，离当前任务距离越远，展示的细节越少。其次是按需加载，skills 基于 markdown+grep，就搭建出一套简单但非常有用的按需加载层。真的是非常优雅。 https://t.co/06p1kuIUO4

![](https://pbs.twimg.com/media/G5r0o9EacAA0zB3.jpg)

## 2
https://x.com/yan5xu/status/1989225126345453702

详细的解释，设计，和借鉴，我拓展成了一篇长文「从《塞尔达传说》到AI Agent：Claude Skills背后的信息分层设计哲学」 
https://t.co/g4GzLUdXcZ
---
