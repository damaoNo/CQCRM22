<template>
    <div>
        <div class="filter-container">
              <el-input
                v-model="searchname"
                class="myInput"
                style="width: 200px;margin-right: 20px"
                suffix-icon="el-icon-search"
                @keyup.enter.native="handleFilter"
                placeholder="请输入套餐名称">
              </el-input>
              <el-button size="small" type="primary"  @click="handleFilter" icon="el-icon-search">搜索</el-button>
              <el-button size="small" style="margin-left: 10px;" @click="handleCreate" type="primary" icon="el-icon-plus">新增</el-button>
        </div>
        <div style="margin-top: 20px">
          <el-table
            :data="list"
            :header-cell-style="{background:'#F8F8F8'}"
            v-loading="listLoading"
            stripe>
            <el-table-column type="index" label="序号"  width="220">
            </el-table-column>
            <el-table-column prop="name" label="名称" width="320">
            </el-table-column>
            <el-table-column prop="type" label="类别" width="200"  align="center">
            </el-table-column>
            <el-table-column prop="id" v-if="false">
            </el-table-column>
            <el-table-column label="操作" fixed="right"  align="center">
              <template slot-scope="scope">
                  <el-button type="text" size="small" @click="handleUpdate(scope.row)">修改</el-button>
                  <el-button type="text" size="small" @click="handleDelete(scope.row)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
          <div class="pagination-container" style="margin-top: 5px" align="right">
                <el-pagination
                  background
                  @current-change="handleCurrentChange"
                  :current-page="listQuery.page"
                  :page-size="listQuery.limit"
                  layout="total, prev, pager, next"
                  :total="total">
                </el-pagination>
          </div>
        </div>

        <div>
          <el-dialog  title="套餐" width="35%" :visible.sync="dialogFormVisible">
              <el-form  :model="tc" ref="dataForm" :rules="rules" label-position="left" label-width="70px" style='width:90%; margin-left:30px;'>
                   <el-row>
                     <el-col>
                        <el-form-item label="名称"  prop="name">
                          <el-input v-model="tc.name" style="width: 350px;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                   </el-row>
                  <el-row>
                     <el-col>
                        <el-form-item label="类型" prop="type">
                          <el-select v-model="tc.type" clearable style="width: 350px" class="myInput">
                            <el-option v-for="item in materialSelect" :key="item.id" :value="item.name" :label="item.name">
                            </el-option>
                          </el-select>
                        </el-form-item>
                      </el-col>
                  </el-row>
              </el-form>
              <div slot="footer" class="dialog-footer">
                <el-button
                  size="small"
                  icon="el-icon-close"
                  @click="dialogFormVisible = false"
                >关闭
                </el-button>
                <el-button
                  size="small"
                  type="primary"
                  icon="el-icon-check"
                  v-if="dialogStatus=='create'"
                  @click="createData">保存
                </el-button>
                <el-button
                  size="small"
                  icon="el-icon-check"
                  v-else type="primary"
                  @click="updateData">保存
                </el-button>
              </div>
          </el-dialog>
        </div>
    </div>
</template>

<script>
import { xyjhdict, xyjhs, createxyjhdict, updatexyjhdict, deletexyjhdict } from '@/api/system'
import { getToken } from '@/utils/auth'
import moment from 'moment'
import ElCol from 'element-ui/packages/col/src/col'
import ElRow from 'element-ui/packages/row/src/row'
import ElTabPane from '../../../node_modules/element-ui/packages/tabs/src/tab-pane'
import ElSlPanel from '../../../node_modules/element-ui/packages/color-picker/src/components/sv-panel'
import ElFormItem from '../../../node_modules/element-ui/packages/form/src/form-item'
import ElRadioGroup from '../../../node_modules/element-ui/packages/radio/src/radio-group'
import ElCheckboxGroup from '../../../node_modules/element-ui/packages/checkbox/src/checkbox-group'
import ElCheckbox from '../../../node_modules/element-ui/packages/checkbox/src/checkbox'
import ElInput from '../../../node_modules/element-ui/packages/input/src/input'

export default {
  components: {
    ElInput,
    ElCheckbox,
    ElCheckboxGroup,
    ElRadioGroup,
    ElFormItem,
    ElSlPanel,
    ElTabPane,
    ElRow,
    ElCol },
  data: function() {
    return {
      list: null,
      total: null,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 10,
        offset: 0,
        name: undefined,
        sort: '+id'
      },
      searchname: '',
      token: getToken,
      dialogFormVisible: false,
      dialogStatus: '',
      materialSelect: [
        { id: '1', name: '医嘱' },
        { id: '2', name: '固定收费' }
      ],
      rules: {
        name: [{ required: true, message: '请输入名称', trigger: 'blur' }],
        type: [{ required: true, message: '请输入类型', trigger: 'blur' }]
      },
      tc: {
        id: null,
        name: '',
        type: ''
      },
      queryparams: {
        page: 1,
        name: ''
      }
    }
  },
  methods: {
    getXyjhdict(data) {
      xyjhdict(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    resetTc() {
      this.tc = {
        id: null,
        name: '',
        type: ''
      }
    },
    handleReset() {
      this.queryparams.page = 1
      this.queryparams.name = ''
      this.searchname = ''
      this.getXyjhdict(this.queryparams)
    },
    handleCreate() {
      this.resetTc()
      this.dialogFormVisible = true
      this.dialogStatus = 'create'
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs.dataForm.validate((valid) => {
        if (valid) {
          this.tc.id = parseInt(Math.random() * 100) + 1024 // mock a id
          createxyjhdict(this.tc).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            this.queryparams.page = 1
            this.getXyjhdict(this.queryparams)
          })
        }
      })
    },
    handleUpdate(row) {
      this.tc = Object.assign({}, row) // copy obj
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.tc)
          updatexyjhdict(tempData).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.queryparams.page = 1
            this.getXyjhdict(this.queryparams)
          })
        }
      })
    },
    handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.tc = Object.assign({}, row) // copy obj
        const tempData = Object.assign({}, this.tc)
        deletexyjhdict(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.queryparams.page = 1
          this.getXyjhdict(this.queryparams)
        })
      })
    },
    handleFilter() {
      this.listQuery.limit = 10
      this.listQuery.offset = 0
      this.queryparams.page = 1
      this.queryparams.name = this.searchname
      this.getXyjhdict(this.queryparams)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.queryparams.page = val
      console.log(this.queryparams)
      this.getXyjhdict(this.queryparams)
    },
    dateFormat: function(row, column) {
      var date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD HH:mm:ss')
    }
  },
  created: function() {
    this.queryparams.page = 1
    this.queryparams.name = ''
    this.getXyjhdict(this.queryparams)
  }
}
</script>

<style>
    .ms-doc{
        width:100%;
        max-width: 980px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    }
    .ms-doc h3{
        padding: 9px 10px 10px;
        margin: 0;
        font-size: 14px;
        line-height: 17px;
        background-color: #f5f5f5;
        border: 1px solid #d8d8d8;
        border-bottom: 0;
        border-radius: 3px 3px 0 0;
    }
    .ms-doc article{
        padding: 45px;
        word-wrap: break-word;
        background-color: #fff;
        border: 1px solid #ddd;
        border-bottom-right-radius: 3px;
        border-bottom-left-radius: 3px;
    }
    .ms-doc article h1{
        font-size:32px;
        padding-bottom: 10px;
        margin-bottom: 15px;
        border-bottom: 1px solid #ddd;
    }
    .ms-doc article h2 {
        margin: 24px 0 16px;
        font-weight: 600;
        line-height: 1.25;
        padding-bottom: 7px;
        font-size: 24px;
        border-bottom: 1px solid #eee;
    }
    .ms-doc article p{
        margin-bottom: 15px;
        line-height: 1.5;
    }
    .ms-doc article .el-checkbox{
        margin-bottom: 5px;
    }
    .myInput .el-input__inner{
        height: 33px;
        border-top-width: 0px;
        border-left-width: 0px;
        border-right-width: 0px;
        border-bottom-width: 1px;
    }
    .el-table td, .el-table th{
      padding:6px 0;
    }
</style>
