DIR = $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
APP = nate_app


build:
	docker image build \
			--rm \
			--tag ${APP} \
			-f Dockerfile .

stop_local_app:
	docker rm -f ${APP} || true

run_app: stop_local_app build
	open http://0.0.0.0:8080/
	docker container run \
	--tty \
	--rm \
	--publish 8080:8080 \
	-v ${DIR}:/${APP} \
	--name ${APP} \
	${APP}

stop_tests:
	docker rm -f ${APP}-unit-tests || true

run_tests: stop_tests build
	docker container run \
	-t \
	--rm \
	--name ${APP}-unit-tests \
	-v ${DIR}:/${APP} \
	${APP} \
	pytest -v /nate_app/app/tests

run_test_coverage: build
	docker container run \
	-t \
	--rm \
	--name ${APP}-test-coverage \
	-v ${DIR}:/${APP} \
	${APP} \
	pytest -cov=project