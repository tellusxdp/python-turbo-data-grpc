import os
import grpc
from grpcturbodata import turbodata_pb2_grpc as pb2_grpc
from grpcturbodata import turbodata_pb2 as pb2

class Const:
    STRING_64 = 64
    STRING_128 = 128
    STRING_256 = 256

    LEN_128 = 128
    LEN_256 = 256
    LEN_512 = 512
    LEN_1024 = 1024
    LEN_4096 = 4096

    # dataTypeConstants
    D5_DT_ERROR, D5_DT_BLANK , D5_DT_INTEGER , D5_DT_DOUBLE , D5_DT_DATE , D5_DT_TIME , D5_DT_STRING , D5_DT_DATETIME , D5_DT_DECIMAL = range(9)
    D5_OPETYPE_EQUAL , D5_OPETYPE_BETWEEN , D5_OPETYPE_LESSEQUAL , D5_OPETYPE_GREATEREQUAL , D5_OPETYPE_NOTEQUAL , D5_OPETYPE_WITHIN , D5_OPETYPE_LESS , D5_OPETYPE_GREATER , D5_OPETYPE_STR_LEFT , D5_OPETYPE_STR_MID , D5_OPETYPE_STR_RIGHT = range(11)
    D5_OPETYPE_NULL = 15
    D5_OPETYPE_NOTNULL = 16

    D5_TABLEKIND_REAL, D5_TABLEKIND_MASTER, D5_TABLEKIND_JOIN = range(3)

    TD_NULL_INT = -0x80000000  # -2147483648
    TD_NULL_NUMERIC = float('-inf')  # Decimal('-Infinity') #-0xff800000
    TD_NULL_DATE = float('-inf')
    TD_NULL_STRING = '(null)'
    TD_NOT_A_REAL_TABLE = -536870775

    SET_OP_AND, SET_OP_OR, SET_OP_SUB, SET_OP_NOT = range(4)

    REC_NO_ID = 0
    REC_NO2_ID = -1
    # arithmeticOperators = {D5_OPETYPE_EQUAL: 'EQUAL', D5_OPETYPE_BETWEEN:'BETWEEN' , D5_OPETYPE_LESSEQUAL, D5_OPETYPE_GREATEREQUAL, D5_OPETYPE_NOTEQUAL, D5_OPETYPE_WITHIN, D5_OPETYPE_LESS, D5_OPETYPE_GREATER}
    arithmeticOperators = {D5_OPETYPE_EQUAL: 'EQUAL', D5_OPETYPE_BETWEEN:'BETWEEN' , D5_OPETYPE_LESSEQUAL:'LESSEQUAL', D5_OPETYPE_GREATEREQUAL:'GREATEREQUAL', D5_OPETYPE_NOTEQUAL:'NOTEQUAL', D5_OPETYPE_WITHIN:'WITHIN', D5_OPETYPE_LESS:'LESS', D5_OPETYPE_GREATER:'GREATER', D5_OPETYPE_NULL:'NULL', D5_OPETYPE_NOTNULL:'NOTNULL'}
    stringOperators = {D5_OPETYPE_STR_LEFT:'STR_LEFT', D5_OPETYPE_STR_MID:'STR_MID', D5_OPETYPE_STR_RIGHT:'STR_RIGHT'}

    dataTypeString = {D5_DT_INTEGER:'Integer', D5_DT_DATETIME:'DateTime', D5_DT_DATE:'Date', D5_DT_TIME:'Time', D5_DT_DOUBLE:'Double', D5_DT_DECIMAL:'Decimal', D5_DT_STRING:'String'}
    dataTypeStrToInt = {'Integer':D5_DT_INTEGER, 'DateTime':D5_DT_DATETIME, 'Date':D5_DT_DATE, 'Time':D5_DT_TIME, 'Double':D5_DT_DOUBLE, 'Decimal':D5_DT_DECIMAL, 'String':D5_DT_STRING}
    setOperators = {0:'AND', 1:'OR', 2:'SUB', SET_OP_NOT:'NOT'}

    D5_SUMMARY_NONE = 0
    D5_SUMMARY_COUNT = 1
    D5_SUMMARY_MAX = 2
    D5_SUMMARY_MIN = 4
    D5_SUMMARY_SUM = 8
    D5_SUMMARY_AVERAGE = 16


class mapPSEngine:

    def __init__(self, address=""):
        if not address:
            address = os.environ.get("TURBODATA_HOST", "localhost:50051")
        self.channel = grpc.insecure_channel(address)
        self.stub = pb2_grpc.DataStoreStub(self.channel)

    def AddRealFilter(self, sTableName, sAddPosition, sNewFilterName, sFilterType, sFilePath, sFileName):
        request = pb2.AddRealFilterRequest(
          tableName = sTableName,
          addPosition = sAddPosition,
          newFilterName = sNewFilterName,
          filterType = sFilterType,
          filePath = sFilePath,
          fileName = sFileName,
        )
        response = self.stub.AddRealFilter(request)
        return response.filterCount

    # rowCount 0 or -1 for all rows starts from iStartRow=1
    def Calc(self, sTableName, sFilterName, iStartRow, iRowCount, sCalcStr, iSetID=1):
        request = pb2.CalcRequest(
          tableName = sTableName,
          filterName = sFilterName,
          startRow = iStartRow,
          rowCount = iRowCount,
          calsStr = sCalcStr,
          setID = iSetID,
        )
        response = self.stub.Calc(request)
        return response.result

    def Catalog(self, sTableName, sCatPath, sCatName, sSrcPath, sSrcName):
        request = pb2.CatalogRequest(
          tableName = sTableName,
          catPath = sCatPath,
          catName = sCatName,
          srcPath = sSrcPath,
          srcName = sSrcName,
        )
        response = self.stub.Catalog(request)
        return response.result

    def Categorize(self, sTableName, sFilterName, sCatTableName):
        request = pb2.CategorizeRequest(
          tableName = sTableName,
          filterName = sFilterName,
          catTableName = sCatTableName,
        )
        response = self.stub.Categorize(request)
        return response.result

    def ClearWS(self):
        response = self.stub.ClearWS(pb2.ClearWSRequest())
        return response.result

    def Condense(self, sTableName):
        request = pb2.CondenseRequest(
          tableName = sTableName,
        )
        response = self.stub.Condense(request)
        return response.result

    def CreateJoin(self, sJTableName, sMTableName, sSTableName, iMSetID, iSSetID, sMJoinKeyList, sSJoinKeyList, sIsInOrOut):
        request = pb2.CreateJoinRequest(
          jTableName = sJTableName,
          mTableName = sMTableName,
          sTableName = sSTableName,
          mSetID = iMSetID,
          sSetID = iSSetID,
          mJoinKeyList = sMJoinKeyList,
          sJoinKeyList = sSJoinKeyList,
          isInOrOut = sIsInOrOut,
        )
        response = self.stub.CreateJoin(request)
        return response.tableID

    def CreateTable(self, iRowCount, sTableName):
        request = pb2.CreateTableRequest(
          rowCount = iRowCount,
          tableName = sTableName,
        )
        response = self.stub.CreateTable(request)
        return response.tableID

    def DBCodeSet(self, sDBCode):
        request = pb2.DBCodeSetRequest(
          dbCode = sDBCode,
        )
        response = self.stub.DBCodeSet(request)
        return response.result

    def DBLoad(self, sFilePath, sWorkSpace):
        request = pb2.DBLoadRequest(
          filePath = sFilePath,
          workSpace = sWorkSpace,
        )
        response = self.stub.DBLoad(request)
        return response.result

    def DBSave(self, sFilePath, sWorkSpace):
        request = pb2.DBSaveRequest(
          filePath = sFilePath,
          workSpace = sWorkSpace,
        )
        response = self.stub.DBSave(request)
        return response.result

    def DelAllSubTables(self, sTableName):
        request = pb2.DelAllSubTablesRequest(
          tableName = sTableName,
        )
        response = self.stub.DelAllSubTables(request)
        return response.result

    def DeleteRow(self, sTableName, iStartRow, iRowCount, iSetID=1):
        request = pb2.DeleteRowRequest(
          tableName = sTableName,
          startRow = iStartRow,
          rowCount = iRowCount,
          setID = iSetID,
        )
        response = self.stub.DeleteRow(request)
        return response.result


    def DelFilter(self, sTableName, sFilterName):
        request = pb2.DelFilterRequest(
          tableName = sTableName,
          filterName = sFilterName,
        )
        response = self.stub.DelFilter(request)
        return response.result

    def Drop(self, sTableName):
        request = pb2.DropRequest(
          tableName = sTableName,
        )
        response = self.stub.Drop(request)
        return response.result

    def DuplFilter(self, sTableName, sFilterName):
        request = pb2.DuplFilterRequest(
          tableName = sTableName,
          filterName = sFilterName,
        )
        response = self.stub.DuplFilter(request)
        return response.result

    def DuplicateTable(self, sTableName):
        request = pb2.DuplicateTableRequest(
          tableName = sTableName,
        )
        response = self.stub.DuplicateTable(request)
        return response.tableID

    def ExtractSubTable(self, sTableName, iSetID, sIncludeTableID, sIncludeRecNo, sFilterNameList, sNewTableName):
        request = pb2.ExtractSubTableRequest(
          tableName = sTableName,
          setID = iSetID,
          includeTableID = sIncludeTableID,
          includeRecNo = sIncludeRecNo,
          filterNameList = sFilterNameList,
          newTableName = sNewTableName,
        )
        response = self.stub.ExtractSubTable(request)
        return response.result


    def ExtractUnique(self, sTableName, iSetID, sFilterNameList, sKeepOrigOrder):
        request = pb2.ExtractUniqueRequest(
          tableName = sTableName,
          setID = iSetID,
          filterNameList = sFilterNameList,
          keepOrigOrder = sKeepOrigOrder,
        )
        response = self.stub.ExtractUnique(request)
        return response.result


    # rowCount 0 or -1 for all rows starts from iStartRow=1
    def Fill(self, sTableName, sFilterName, iStartRow, iRowCount, sDataToUpdate, iSetID):
        request = pb2.FillRequest(
          tableName = sTableName,
          filterName = sFilterName,
          startRow = iStartRow,
          rowCount = iRowCount,
          dataToUpdate = sDataToUpdate,
          setID = iSetID,
        )
        response = self.stub.Fill(request)
        return response.result

    def FilterTransfer(self, sTableName, sSlaveFilterList):
        request = pb2.FilterTransferRequest(
          tableName = sTableName,
          slaveFilterList = sSlaveFilterList,
        )
        response = self.stub.FilterTransfer(request)
        return response.result

    def InsertRow(self, sTableName, iStartRow, iRowCount):
        request = pb2.InsertRowRequest(
          tableName = sTableName,
          startRow = iStartRow,
          rowCount = iRowCount,
        )
        response = self.stub.InsertRow(request)
        return response.result

    def JoinRealize(self, sNewTableName, sRTablename, iSetID, sMRecNo, sSRecNo, sFilterNameList):
        request = pb2.JoinRealizeRequest(
          newTableName = sNewTableName,
          rTablename = sRTablename,
          setID = iSetID,
          mRecNo = sMRecNo,
          sRecNo = sSRecNo,
          filterNameList = sFilterNameList,
        )
        response = self.stub.JoinRealize(request)
        return response.result

    def Load(self, sFilePath, sTableName):
        request = pb2.LoadRequest(
          filePath = sFilePath,
          tableName = sTableName,
        )
        response = self.stub.Load(request)
        return response.tableID

    def MoveFilter(self, sTableName, sFilterFrom, sFilterTo):
        request = pb2.MoveFilterRequest(
          tableName = sTableName,
          filterFrom = sFilterFrom,
          filterTo = sFilterTo,
        )
        response = self.stub.MoveFilter(request)
        return response.result

    def Rename(self, sTableName, sNewTableName):
        request = pb2.RenameRequest(
          tableName = sTableName,
          newTableName = sNewTableName,
        )
        response = self.stub.Rename(request)
        return response.result


    def RenameFilter(self, sTableName, sFilterName, sNewFilterName):
        request = pb2.RenameFilterRequest(
          tableName = sTableName,
          filterName = sFilterName,
          newFilterName = sNewFilterName,
        )
        response = self.stub.RenameFilter(request)
        return response.result

    def Save(self, sFilePath, sTableName):
        request = pb2.SaveRequest(
          filePath = sFilePath,
          tableName = sTableName,
        )
        response = self.stub.Save(request)
        return response.result


    def Search(self, sTableName, sFilterName, iSetID, sSrcString):
        request = pb2.SearchRequest(
          tableName = sTableName,
          filterName = sFilterName,
          setID = iSetID,
          srcString = sSrcString,
        )
        response = self.stub.Search(request)
        return response.result


    def SetAND(self, sTableName, iSetID, iDestSetID):
        request = pb2.SetANDRequest(
          tableName = sTableName,
          setID = iSetID,
          destSetID = iDestSetID,
        )
        response = self.stub.SetAND(request)
        return response.result

    def SetNOT(self, sTableName, iSetID, iDestSetID):
        request = pb2.SetNOTRequest(
          tableName = sTableName,
          setID = iSetID,
          destSetID = iDestSetID,
        )
        response = self.stub.SetNOT(request)
        return response.result


    def SetOR(self, sTableName, iSetID, iDestSetID):
        request = pb2.SetORRequest(
          tableName = sTableName,
          setID = iSetID,
          destSetID = iDestSetID,
        )
        response = self.stub.SetOR(request)
        return response.result


    def SetSUB(self, sTableName, iSetID, iDestSetID):
        request = pb2.SetSUBRequest(
          tableName = sTableName,
          setID = iSetID,
          destSetID = iDestSetID,
        )
        response = self.stub.SetSUB(request)
        return response.result


    def SetComment(self, sTableName, iSetID, sCmntStr):
        request = pb2.SetCommentRequest(
          tableName = sTableName,
          setID = iSetID,
          cmntStr = sCmntStr,
        )
        response = self.stub.SetComment(request)
        return response.result


    def SetDelete(self, sTableName, iSetID):
        request = pb2.SetDeleteRequest(
          tableName = sTableName,
          setID = iSetID,
        )
        response = self.stub.SetDelete(request)
        return response.result

    def Sort(self, sTableName, sFilterName, iSetID, sSortType):
        request = pb2.SortRequest(
          tableName = sTableName,
          filterName = sFilterName,
          setID = iSetID,
          sortType = sSortType,
        )
        response = self.stub.Sort(request)
        return response.result


    # for all iWriteTop = 1, iWriteBottom = -1, iWriteLeft =1, iWriteRight = -1
    def TextWrite(self, sTableName, sDelimiter, sFilePath, sFileName, iWriteTop, iWriteBottom, iWriteLeft, iWriteRight, sHeader, iSetID):
        request = pb2.TextWriteRequest(
          tableName = sTableName,
          delimiter = sDelimiter,
          filePath = sFilePath,
          fileName = sFileName,
          writeTop = iWriteTop,
          writeBottom = iWriteBottom,
          writeLeft = iWriteLeft,
          writeRight = iWriteRight,
          header = sHeader,
          setID = iSetID,
        )
        response = self.stub.TextWrite(request)
        return response.result


    def Union(self, sNewTableName, sTableName1, sTableName2, iSetID1, iSetid2, sFilterIDs1, sFilterIDs2, sIncludeTableID, sIncludeRecordNo, sDeleteOriginal):
        request = pb2.UnionRequest(
          newTableName = sNewTableName,
          tableName1 = sTableName1,
          tableName2 = sTableName2,
          setID1 = iSetID1,
          setID2 = iSetID2,
          filterIDs1 = sFilterIDs1,
          filterIDs2 = sFilterIDs2,
          includeTableID = sIncludeTableID,
          includeRecordNo = sIncludeRecordNo,
          deleteOriginal = sDeleteOriginal,
        )
        response = self.stub.Union(request)
        return response.tableID


    def XSum(self, sTableName, iSetID, sDItemList, sMItemList):
        request = pb2.XSumRequest(
          tableName = sTableName,
          setID = iSetID,
          dItemList = sDItemList,
          mItemList = sMItemList,
        )
        response = self.stub.XSum(request)
        return response.tableID
