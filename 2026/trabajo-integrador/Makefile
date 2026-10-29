.PHONY: all pdf paquetes

DOCUMENTOS := consigna propuesta informe

all: pdf paquetes

pdf:
	mkdir -p build pdf
	@for documento in $(DOCUMENTOS); do \
		latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build "$$documento.tex" || exit $$?; \
		cp "build/$$documento.pdf" "pdf/$$documento.pdf"; \
	done

paquetes:
	mkdir -p build/overleaf/propuesta build/overleaf/informe distribucion
	cp propuesta.tex build/overleaf/propuesta/main.tex
	cp informe.tex build/overleaf/informe/main.tex
	cp estilo.tex build/overleaf/propuesta/estilo.tex
	cp estilo.tex build/overleaf/informe/estilo.tex
	cd build/overleaf/propuesta && zip -q ../../../distribucion/propuesta-overleaf.zip main.tex estilo.tex
	cd build/overleaf/informe && zip -q ../../../distribucion/informe-overleaf.zip main.tex estilo.tex
