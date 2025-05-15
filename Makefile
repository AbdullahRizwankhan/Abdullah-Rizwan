
PAGES=$(wildcard pages/*.html) # wildcard permet d'utiliser l'étoile pour lister des fichiers
ASSETS=$(wildcard assets/*) 
PUBLIC_PAGES= $(subst pages/,public/,$(PAGES))# subst fait une substitution dans chaque élément de la liste

all: public $(PUBLIC_PAGES)
.PHONY: all clean public



public/%.html: pages/%.html layout/before.html layout/after.html
	./scripts/buildpage.sh $< layout/before.html layout/after.html > $@

public:
	mkdir -p public
	cp -u $(ASSETS) public/ 
	touch public

	


clean:
	rm -rf public

