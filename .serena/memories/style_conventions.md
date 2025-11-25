# 代码风格与规范
- flake8：忽略 W503/W504，最大行宽 120。
- yapf：基于 pep8，列宽 120，类/函数前空行，开启 split_before_expression_after_opening_paren。
- isort：行宽 120，first party `gfpgan`，第三方含 basicsr、torch 等。
- 命名/设计：遵循 README/AGENTS 指南，强调单一职责、显式依赖、避免花哨写法，必要注释用简短中文说明。
- 兼容性：在新增入口中先调用 `gfpgan.torchvision_compat.ensure_legacy_torchvision_support()` 再导入 Basicsr/torchvision 相关代码。