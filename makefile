ifeq ($(shell id -u), 0)
	EXTENSION_DIR = /usr/share/nautilus-python/extensions
	SCHEMA_DIR = /usr/share/glib-2.0/schemas
else
	EXTENSION_DIR = ~/.local/share/nautilus-python/extensions
	SCHEMA_DIR = ~/.local/share/glib-2.0/schemas
endif

install:
	install -d $(EXTENSION_DIR)
	install Back.py $(EXTENSION_DIR)

	install -d $(SCHEMA_DIR)
	install io.github.alt-gnome-team.nautilus-backspace.gschema.xml $(SCHEMA_DIR)

schemas:
	glib-compile-schemas $(SCHEMA_DIR)