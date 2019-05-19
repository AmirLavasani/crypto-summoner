# import json
# import xml.etree.ElementTree as et 

# class JsonSerializer:
#     def __init__(self):
#         self._current_object = None

#     def start_object(self, object_name, object_id):
#         self._current_object = {
#             'id': object_id
#         }

#     def add_property(self, name, value):
#         self._current_object[name] = value

#     def to_str(self):
#         return json.dumps(self._current_object)


# class XmlSerializer:
#     def __init__(self):
#         self._element = None

#     def start_object(self, object_name, object_id):
#         self._element = et.Element(object_name, attrib={'id': object_id})

#     def add_property(self, name, value):
#         prop = et.SubElement(self._element, name)
#         prop.text = value

#     def to_str(self):
#         return et.tostring(self._element, encoding='unicode')

# class ObjectSerializer:
#     def serialize(self, serializable, format):
#         serializer = factory.get_serializer(format)
#         serializable.serialize(serializer)
#         return serializer.to_str()

# class Song:
#     def __init__(self, song_id, title, artist):
#         self.song_id = song_id
#         self.title = title
#         self.artist = artist

#     def serialize(self, serializer):
#         serializer.start_object('song', self.song_id)
#         serializer.add_property('title', self.title)
#         serializer.add_property('artist', self.artist)

# class SerializerFactory:
#     def __init__(self):
#         self._creators = {}

#     def register_format(self, format, creator):
#         self._creators[format] = creator

#     def get_serializer(self, format):
#         creator = self._creators.get(format)
#         if not creator:
#             raise ValueError(format)
#         return creator()

# factory = SerializerFactory()
# factory.register_format('JSON', JsonSerializer)
# factory.register_format('XML', XmlSerializer)

# # import yaml

# # class YamlSerializer(serializers.JsonSerializer):
# #     def to_str(self):
# #         return yaml.dump(self._current_object)


# # serializers.factory.register_format('YAML', YamlSerializer)


import sys

# Colored printing functions for strings that use universal ANSI escape sequences.
# fail: bold red, pass: bold green, warn: bold yellow, 
# info: bold blue, bold: bold white

class ColorPrint:

    @staticmethod
    def print_fail(message, end = '\n'):
        sys.stderr.write('\x1b[1;31m' + message.strip() + '\x1b[0m' + end)

    @staticmethod
    def print_pass(message, end = '\n'):
        sys.stdout.write('\x1b[1;32m' + message.strip() + '\x1b[0m' + end)

    @staticmethod
    def print_warn(message, end = '\n'):
        sys.stderr.write('\x1b[1;33m' + message.strip() + '\x1b[0m' + end)

    @staticmethod
    def print_info(message, end = '\n'):
        sys.stdout.write('\x1b[1;34m' + message.strip() + '\x1b[0m' + end)

    @staticmethod
    def print_bold(message, end = '\n'):
        sys.stdout.write('\x1b[1;37m' + message.strip() + '\x1b[0m' + end)

ColorPrint.print_pass('123')