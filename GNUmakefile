#
.DEFAULT_GOAL:=		test

clean:
	rm -f *.retry

deploy:
	ansible-playbook newspaper.hasname.com.yml

push:
	git push -v origin master

test:
	true
