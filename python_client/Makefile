protoc:
	poetry run python -m grpc_tools.protoc \
		--python_out=./ \
		--grpc_python_out=./ \
		--proto_path=../python_server/ \
		../python_server/**/*.proto
