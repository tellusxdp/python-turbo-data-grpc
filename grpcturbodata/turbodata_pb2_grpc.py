# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from grpcturbodata import turbodata_pb2 as turbodata_dot_grpc_dot_turbodata__pb2


class DataSourceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.AddRealFilter = channel.unary_unary(
        '/turbodata.DataSource/AddRealFilter',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.AddRealFilterRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.AddRealFilterResponse.FromString,
        )
    self.Calc = channel.unary_unary(
        '/turbodata.DataSource/Calc',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.CalcRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.CalcResponse.FromString,
        )
    self.Catalog = channel.unary_unary(
        '/turbodata.DataSource/Catalog',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.CatalogRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.CatalogResponse.FromString,
        )
    self.Categorize = channel.unary_unary(
        '/turbodata.DataSource/Categorize',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.CategorizeRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.CategorizeResponse.FromString,
        )
    self.ClearWS = channel.unary_unary(
        '/turbodata.DataSource/ClearWS',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.ClearWSRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.ClearWSResponse.FromString,
        )
    self.Condense = channel.unary_unary(
        '/turbodata.DataSource/Condense',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.CondenseRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.CondenseResponse.FromString,
        )
    self.CreateJoin = channel.unary_unary(
        '/turbodata.DataSource/CreateJoin',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.CreateJoinRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.CreateJoinResponse.FromString,
        )
    self.CreateTable = channel.unary_unary(
        '/turbodata.DataSource/CreateTable',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.CreateTableRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.CreateTableResponse.FromString,
        )
    self.DBCodeSet = channel.unary_unary(
        '/turbodata.DataSource/DBCodeSet',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.DBCodeSetRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.DBCodeSetResponse.FromString,
        )
    self.DBLoad = channel.unary_unary(
        '/turbodata.DataSource/DBLoad',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.DBLoadRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.DBLoadResponse.FromString,
        )
    self.DBSave = channel.unary_unary(
        '/turbodata.DataSource/DBSave',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.DBSaveRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.DBSaveResponse.FromString,
        )
    self.DelAllSubTables = channel.unary_unary(
        '/turbodata.DataSource/DelAllSubTables',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.DelAllSubTablesRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.DelAllSubTablesResponse.FromString,
        )
    self.DeleteRow = channel.unary_unary(
        '/turbodata.DataSource/DeleteRow',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.DeleteRowRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.DeleteRowResponse.FromString,
        )
    self.DelFilter = channel.unary_unary(
        '/turbodata.DataSource/DelFilter',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.DelFilterRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.DelFilterResponse.FromString,
        )
    self.Drop = channel.unary_unary(
        '/turbodata.DataSource/Drop',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.DropRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.DropResponse.FromString,
        )
    self.DuplFilter = channel.unary_unary(
        '/turbodata.DataSource/DuplFilter',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.DuplFilterRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.DuplFilterResponse.FromString,
        )
    self.DuplicateTable = channel.unary_unary(
        '/turbodata.DataSource/DuplicateTable',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.DuplicateTableRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.DuplicateTableResponse.FromString,
        )
    self.ExtractSubTable = channel.unary_unary(
        '/turbodata.DataSource/ExtractSubTable',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.ExtractSubTableRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.ExtractSubTableResponse.FromString,
        )
    self.ExtractUnique = channel.unary_unary(
        '/turbodata.DataSource/ExtractUnique',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.ExtractUniqueRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.ExtractUniqueResponse.FromString,
        )
    self.Fill = channel.unary_unary(
        '/turbodata.DataSource/Fill',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.FillRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.FillResponse.FromString,
        )
    self.FilterTransfer = channel.unary_unary(
        '/turbodata.DataSource/FilterTransfer',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.FilterTransferRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.FilterTransferResponse.FromString,
        )
    self.InsertRow = channel.unary_unary(
        '/turbodata.DataSource/InsertRow',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.InsertRowRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.InsertRowResponse.FromString,
        )
    self.JoinRealize = channel.unary_unary(
        '/turbodata.DataSource/JoinRealize',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.JoinRealizeRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.JoinRealizeResponse.FromString,
        )
    self.Load = channel.unary_unary(
        '/turbodata.DataSource/Load',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.LoadRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.LoadResponse.FromString,
        )
    self.MoveFilter = channel.unary_unary(
        '/turbodata.DataSource/MoveFilter',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.MoveFilterRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.MoveFilterResponse.FromString,
        )
    self.Rename = channel.unary_unary(
        '/turbodata.DataSource/Rename',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.RenameRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.RenameResponse.FromString,
        )
    self.RenameFilter = channel.unary_unary(
        '/turbodata.DataSource/RenameFilter',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.RenameFilterRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.RenameFilterResponse.FromString,
        )
    self.Save = channel.unary_unary(
        '/turbodata.DataSource/Save',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.SaveRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.SaveResponse.FromString,
        )
    self.Search = channel.unary_unary(
        '/turbodata.DataSource/Search',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.SearchRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.SearchResponse.FromString,
        )
    self.SetAND = channel.unary_unary(
        '/turbodata.DataSource/SetAND',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.SetANDRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.SetANDResponse.FromString,
        )
    self.SetComment = channel.unary_unary(
        '/turbodata.DataSource/SetComment',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.SetCommentRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.SetCommentResponse.FromString,
        )
    self.SetDelete = channel.unary_unary(
        '/turbodata.DataSource/SetDelete',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.SetDeleteRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.SetDeleteResponse.FromString,
        )
    self.SetNOT = channel.unary_unary(
        '/turbodata.DataSource/SetNOT',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.SetNOTRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.SetNOTResponse.FromString,
        )
    self.SetOR = channel.unary_unary(
        '/turbodata.DataSource/SetOR',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.SetORRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.SetORResponse.FromString,
        )
    self.SetSUB = channel.unary_unary(
        '/turbodata.DataSource/SetSUB',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.SetSUBRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.SetSUBResponse.FromString,
        )
    self.Sort = channel.unary_unary(
        '/turbodata.DataSource/Sort',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.SortRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.SortResponse.FromString,
        )
    self.TextWrite = channel.unary_unary(
        '/turbodata.DataSource/TextWrite',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.TextWriteRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.TextWriteResponse.FromString,
        )
    self.Union = channel.unary_unary(
        '/turbodata.DataSource/Union',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.UnionRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.UnionResponse.FromString,
        )
    self.XSum = channel.unary_unary(
        '/turbodata.DataSource/XSum',
        request_serializer=turbodata_dot_grpc_dot_turbodata__pb2.XSumRequest.SerializeToString,
        response_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.XSumResponse.FromString,
        )


class DataSourceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def AddRealFilter(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Calc(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Catalog(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Categorize(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ClearWS(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Condense(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateJoin(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateTable(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DBCodeSet(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DBLoad(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DBSave(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DelAllSubTables(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteRow(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DelFilter(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Drop(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DuplFilter(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DuplicateTable(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ExtractSubTable(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ExtractUnique(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Fill(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FilterTransfer(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InsertRow(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def JoinRealize(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Load(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MoveFilter(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Rename(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RenameFilter(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Save(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Search(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetAND(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetComment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetDelete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetNOT(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetOR(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetSUB(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Sort(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TextWrite(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Union(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def XSum(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DataSourceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'AddRealFilter': grpc.unary_unary_rpc_method_handler(
          servicer.AddRealFilter,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.AddRealFilterRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.AddRealFilterResponse.SerializeToString,
      ),
      'Calc': grpc.unary_unary_rpc_method_handler(
          servicer.Calc,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.CalcRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.CalcResponse.SerializeToString,
      ),
      'Catalog': grpc.unary_unary_rpc_method_handler(
          servicer.Catalog,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.CatalogRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.CatalogResponse.SerializeToString,
      ),
      'Categorize': grpc.unary_unary_rpc_method_handler(
          servicer.Categorize,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.CategorizeRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.CategorizeResponse.SerializeToString,
      ),
      'ClearWS': grpc.unary_unary_rpc_method_handler(
          servicer.ClearWS,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.ClearWSRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.ClearWSResponse.SerializeToString,
      ),
      'Condense': grpc.unary_unary_rpc_method_handler(
          servicer.Condense,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.CondenseRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.CondenseResponse.SerializeToString,
      ),
      'CreateJoin': grpc.unary_unary_rpc_method_handler(
          servicer.CreateJoin,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.CreateJoinRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.CreateJoinResponse.SerializeToString,
      ),
      'CreateTable': grpc.unary_unary_rpc_method_handler(
          servicer.CreateTable,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.CreateTableRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.CreateTableResponse.SerializeToString,
      ),
      'DBCodeSet': grpc.unary_unary_rpc_method_handler(
          servicer.DBCodeSet,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.DBCodeSetRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.DBCodeSetResponse.SerializeToString,
      ),
      'DBLoad': grpc.unary_unary_rpc_method_handler(
          servicer.DBLoad,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.DBLoadRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.DBLoadResponse.SerializeToString,
      ),
      'DBSave': grpc.unary_unary_rpc_method_handler(
          servicer.DBSave,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.DBSaveRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.DBSaveResponse.SerializeToString,
      ),
      'DelAllSubTables': grpc.unary_unary_rpc_method_handler(
          servicer.DelAllSubTables,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.DelAllSubTablesRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.DelAllSubTablesResponse.SerializeToString,
      ),
      'DeleteRow': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteRow,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.DeleteRowRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.DeleteRowResponse.SerializeToString,
      ),
      'DelFilter': grpc.unary_unary_rpc_method_handler(
          servicer.DelFilter,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.DelFilterRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.DelFilterResponse.SerializeToString,
      ),
      'Drop': grpc.unary_unary_rpc_method_handler(
          servicer.Drop,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.DropRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.DropResponse.SerializeToString,
      ),
      'DuplFilter': grpc.unary_unary_rpc_method_handler(
          servicer.DuplFilter,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.DuplFilterRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.DuplFilterResponse.SerializeToString,
      ),
      'DuplicateTable': grpc.unary_unary_rpc_method_handler(
          servicer.DuplicateTable,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.DuplicateTableRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.DuplicateTableResponse.SerializeToString,
      ),
      'ExtractSubTable': grpc.unary_unary_rpc_method_handler(
          servicer.ExtractSubTable,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.ExtractSubTableRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.ExtractSubTableResponse.SerializeToString,
      ),
      'ExtractUnique': grpc.unary_unary_rpc_method_handler(
          servicer.ExtractUnique,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.ExtractUniqueRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.ExtractUniqueResponse.SerializeToString,
      ),
      'Fill': grpc.unary_unary_rpc_method_handler(
          servicer.Fill,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.FillRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.FillResponse.SerializeToString,
      ),
      'FilterTransfer': grpc.unary_unary_rpc_method_handler(
          servicer.FilterTransfer,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.FilterTransferRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.FilterTransferResponse.SerializeToString,
      ),
      'InsertRow': grpc.unary_unary_rpc_method_handler(
          servicer.InsertRow,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.InsertRowRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.InsertRowResponse.SerializeToString,
      ),
      'JoinRealize': grpc.unary_unary_rpc_method_handler(
          servicer.JoinRealize,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.JoinRealizeRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.JoinRealizeResponse.SerializeToString,
      ),
      'Load': grpc.unary_unary_rpc_method_handler(
          servicer.Load,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.LoadRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.LoadResponse.SerializeToString,
      ),
      'MoveFilter': grpc.unary_unary_rpc_method_handler(
          servicer.MoveFilter,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.MoveFilterRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.MoveFilterResponse.SerializeToString,
      ),
      'Rename': grpc.unary_unary_rpc_method_handler(
          servicer.Rename,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.RenameRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.RenameResponse.SerializeToString,
      ),
      'RenameFilter': grpc.unary_unary_rpc_method_handler(
          servicer.RenameFilter,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.RenameFilterRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.RenameFilterResponse.SerializeToString,
      ),
      'Save': grpc.unary_unary_rpc_method_handler(
          servicer.Save,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.SaveRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.SaveResponse.SerializeToString,
      ),
      'Search': grpc.unary_unary_rpc_method_handler(
          servicer.Search,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.SearchRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.SearchResponse.SerializeToString,
      ),
      'SetAND': grpc.unary_unary_rpc_method_handler(
          servicer.SetAND,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.SetANDRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.SetANDResponse.SerializeToString,
      ),
      'SetComment': grpc.unary_unary_rpc_method_handler(
          servicer.SetComment,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.SetCommentRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.SetCommentResponse.SerializeToString,
      ),
      'SetDelete': grpc.unary_unary_rpc_method_handler(
          servicer.SetDelete,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.SetDeleteRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.SetDeleteResponse.SerializeToString,
      ),
      'SetNOT': grpc.unary_unary_rpc_method_handler(
          servicer.SetNOT,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.SetNOTRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.SetNOTResponse.SerializeToString,
      ),
      'SetOR': grpc.unary_unary_rpc_method_handler(
          servicer.SetOR,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.SetORRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.SetORResponse.SerializeToString,
      ),
      'SetSUB': grpc.unary_unary_rpc_method_handler(
          servicer.SetSUB,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.SetSUBRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.SetSUBResponse.SerializeToString,
      ),
      'Sort': grpc.unary_unary_rpc_method_handler(
          servicer.Sort,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.SortRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.SortResponse.SerializeToString,
      ),
      'TextWrite': grpc.unary_unary_rpc_method_handler(
          servicer.TextWrite,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.TextWriteRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.TextWriteResponse.SerializeToString,
      ),
      'Union': grpc.unary_unary_rpc_method_handler(
          servicer.Union,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.UnionRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.UnionResponse.SerializeToString,
      ),
      'XSum': grpc.unary_unary_rpc_method_handler(
          servicer.XSum,
          request_deserializer=turbodata_dot_grpc_dot_turbodata__pb2.XSumRequest.FromString,
          response_serializer=turbodata_dot_grpc_dot_turbodata__pb2.XSumResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'turbodata.DataSource', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
