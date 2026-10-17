# Repository Reconciliation

正式仓库https://github.com/loverlike1216/SonoField-FPGA.git；当前工作区
E:\Codex_project\AMD_Sonofield；唯一活动v5，分支codex/v5-hardware-design-20261011。
起点PR4 HEAD618b6f1ffe3dae9b98c59bf1c981349e48644662。
本轮开始fetch后的main为ecd32e76e9b6c08806eae30a3c75a9c3be5e7570。

PR1 d7f7b60 → PR2 7dda49f → PR3 b08ccf5 → PR4 618b6f1的祖先关系由
git merge-base --is-ancestor及merge-base实际验证。四个PR均OPEN/Draft/未合并。
新PR叠加PR4分支，不能称已进入main。完整API字段见同名JSON。

原始沙盒没有访问。Historical project仅比较3918条Git树/index的
blob/mode/path元数据，没有读取正文。当前代码/测试/证据4641原始文件
单独哈希快照在BEFORE_CHANGE_HASHES.json。运行源只来自当前v5。

用户明确授权本轮自行同步GitHub；按正常commit/push执行。尚有P0工程风险，
因此不自动把制造前候选当成main发布；不是因常规提交缺少用户权限。
实际最终远端SHA、PR与CI以shared/hardware_design/PUBLICATION_RECEIPT.json为准。
