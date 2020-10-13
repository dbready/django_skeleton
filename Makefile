.PHONY: help build clean

help :
	echo "Don't do foolish things"

build :
	buildah bud --layers --build-arg GIT_COMMIT=$(git rev-parse HEAD) --tag skeleton:latest skeleton
	# buildah fails if attempting to push over existing
	rm -rf build/images/skeleton-latest.tar
	buildah push skeleton:latest docker-archive:build/images/skeleton-latest.tar

clean :
	rm -rf build/
