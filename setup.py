from setuptools import setup, find_packages

# 패키지 메타데이터 설정
setup(
    name='databricks_test_library',  # 패키지 이름
    version='0.1.0',  # 버전
    packages=find_packages(include=["lbox_test", "lbox_test.*"]),  # 패키지 목록 자동 검색    
)