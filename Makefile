SHELL=/usr/bin/env bash
PROJECT_NAME=worker-stable_diffusion
BRANCH_NAME=$(shell if [ -z $$BRANCH_NAME ]; then git symbolic-ref -q --short HEAD; else echo $$BRANCH_NAME; fi)
DOCKER_REPO=jwmarshall

docker-image:
	@docker buildx build -t $(PROJECT_NAME):$(BRANCH_NAME) .

docker-tag:
	@docker tag $(PROJECT_NAME):$(BRANCH_NAME) $(DOCKER_REPO)/$(PROJECT_NAME):$(BRANCH_NAME)

docker-push: docker-tag
	@docker push $(DOCKER_REPO)/$(PROJECT_NAME):$(BRANCH_NAME)
