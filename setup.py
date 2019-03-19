from setuptools import setup

setup(
    name='grpc-turbodata',
    version='0.0.1',
    description='package for Turbo Data gRPC Client',
    author='Yota EGUSA',
    author_email='y-egusa@sakura.ad.jp',
    url='https://github.com/tellusxdp/python-turbo-data-grpc',
    packages=["grpcturbodata", "grpcturbodata.v1"],
    include_package_data=True,
)
