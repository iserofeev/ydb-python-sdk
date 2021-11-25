# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kikimr/public/api/grpc/ydb_monitoring_v1.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kikimr.public.api.protos import ydb_monitoring_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__monitoring__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kikimr/public/api/grpc/ydb_monitoring_v1.proto',
  package='Ydb.Monitoring.V1',
  syntax='proto3',
  serialized_options=b'\n\034com.yandex.ydb.monitoring.v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n.kikimr/public/api/grpc/ydb_monitoring_v1.proto\x12\x11Ydb.Monitoring.V1\x1a-kikimr/public/api/protos/ydb_monitoring.proto2e\n\x11MonitoringService\x12P\n\tSelfCheck\x12 .Ydb.Monitoring.SelfCheckRequest\x1a!.Ydb.Monitoring.SelfCheckResponseB\x1e\n\x1c\x63om.yandex.ydb.monitoring.v1b\x06proto3'
  ,
  dependencies=[kikimr_dot_public_dot_api_dot_protos_dot_ydb__monitoring__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_MONITORINGSERVICE = _descriptor.ServiceDescriptor(
  name='MonitoringService',
  full_name='Ydb.Monitoring.V1.MonitoringService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=116,
  serialized_end=217,
  methods=[
  _descriptor.MethodDescriptor(
    name='SelfCheck',
    full_name='Ydb.Monitoring.V1.MonitoringService.SelfCheck',
    index=0,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__monitoring__pb2._SELFCHECKREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_ydb__monitoring__pb2._SELFCHECKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MONITORINGSERVICE)

DESCRIPTOR.services_by_name['MonitoringService'] = _MONITORINGSERVICE

# @@protoc_insertion_point(module_scope)