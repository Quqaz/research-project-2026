import os

# 研究项目信息
PROJECT_NAME = "Digital_Tools_Research"
# 这里改成你自己的ORCID地址
ORCID_ID = "https://orcid.org/0009-0009-5010-5701"

def initialize_ecosystem():
    print("=== 开始初始化项目结构 ===")
    
    # 自动创建规定文件夹
    directories = ['data/raw', 'data/processed', 'scripts', 'bib', 'docs']
    
    for folder in directories:
        os.makedirs(folder, exist_ok=True)
        print(f"✅ Created/Checked: {folder}")
    
    # 自动生成README说明文档
    readme_content = f"""# {PROJECT_NAME}

## 研究者信息
- **ORCID:** {ORCID_ID}

## 项目文件夹结构
- `data/`: 研究数据集
- `scripts/`: 代码脚本
- `bib/`: 参考文献bib文件
- `docs/`: 项目文档草稿

*由init_research.py自动生成*
"""
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
        print("✅ README.md 已生成/更新")
    
    print("=== 执行成功：项目文件夹与说明文档已生成 ===")

if __name__ == "__main__":
    print("脚本已启动...")
    initialize_ecosystem()
    print("脚本执行完成！")