#encoding:utf-8

class Geom:
    def __init__(self):
        rec={}
        rec['nav_link']="SELECT geom from nav_link where link_id = test_feature_id;"
        rec['nav_link_limit']="select nl.geom from nav_link nl, nav_link_limit nll where  link_limit_id = test_feature_id and nll.link_id = nl.link_id;"
        rec['nav_link_sspeed']="select nl.geom from nav_link nl, nav_link_sspeed nls where  link_sspeed_id = test_feature_id and nls.link_id = nl.link_id;"
        rec['nav_link_zone']="select nl.geom from nav_link nl, nav_link_zone nlz where  link_zone_id = test_feature_id and nlz.link_id = nl.link_id;"
        rec['nav_link_name']="select nl.geom from nav_link nl, nav_link_name nln where link_name_id = test_feature_id and nln.link_id = nl.link_id;"
        rec['nav_name']="select nl.geom from nav_link nl, nav_link_name nln, nav_name nn where nn.name_id = test_feature_id and nln.link_id = nl.link_id and nn.name_id = nln.name_id;"
        rec['nav_node']="select nn.geom from nav_node nn where node_id = test_feature_id;"
        rec['nav_slope']="select ST_Collect(nl.geom, nn.geom) from nav_slope ns, nav_link nl, nav_node nn where  slope_id = test_feature_id and nn.node_id = ns.node_id and nl.link_id = ns.link_id;"
        rec['nav_camera']="select nc.geom from nav_camera nc where camera_id = test_feature_id;"
        rec['nav_warninginfo']="select ST_Collect(nl.geom, nn.geom) from nav_warninginfo nw, nav_link nl, nav_node nn where nw.warn_id =test_feature_id and nn.node_id = nw.node_id and nl.link_id = nw.link_id;"
        rec['nav_directroute']="select ST_Collect(ST_Collect(nl_1.geom, nn.geom), nl_2.geom) from nav_directroute nd, nav_link nl_1, nav_link nl_2, nav_node nn where nd.direct_id=test_feature_id and nn.node_id = nd.node_id and nl_1.link_id = nd.in_linkid and nl_2.link_id = nd.out_linkid;"
        rec['nav_directroute_pass']="select nl.geom from nav_link nl, nav_directroute_pass ndp where ndp.direct_pass_id=test_feature_id and ndp.link_id = nl.link_id;"
        rec['nav_gate']="select ST_Collect(ST_Collect(nl_1.geom, nn.geom), nl_2.geom) from nav_gate ng, nav_link nl_1, nav_link nl_2, nav_node nn where ng.gate_id =test_feature_id and nn.node_id = ng.node_id and nl_1.link_id = ng.in_linkid and nl_2.link_id = ng.out_linkid;"
        rec['nav_gate_cond']="select ST_Collect(ST_Collect(nl_1.geom, nn.geom), nl_2.geom) from nav_gate_cond ngc, nav_gate ng, nav_link nl_1, nav_link nl_2, nav_node nn where ngc.gate_cond_id =test_feature_id and ngc.gate_id = ng.gate_id and nn.node_id = ng.node_id and nl_1.link_id = ng.in_linkid and nl_2.link_id = ng.out_linkid;"
        rec['nav_se']="select ST_Collect(ST_Collect(nl_1.geom, nn.geom), nl_2.geom) from nav_se ns, nav_link nl_1, nav_link nl_2, nav_node nn where ns.se_id = test_feature_id and nn.node_id = ns.node_id and nl_1.link_id = ns.in_linkid and nl_2.link_id = ns.out_linkid;"
        rec['nav_trafficsignal']="select ST_Collect(nl.geom, nn.geom) from nav_trafficsignal nt, nav_link nl, nav_node nn where nt.signal_id = test_feature_id and nn.node_id = nt.node_id and nl.link_id = nt.link_id;"
        rec['nav_tollgate']="select ST_Collect(ST_Collect(nl_1.geom, nn.geom), nl_2.geom) from nav_tollgate nt, nav_link nl_1, nav_link nl_2, nav_node nn where  nt.toll_id = test_feature_id and nn.node_id = nt.node_id and nl_1.link_id = nt.in_linkid and nl_2.link_id = nt.out_linkid;"
        rec['nav_tollgate_passage']="select ST_Collect(ST_Collect(nl_1.geom, nn.geom), nl_2.geom) from nav_tollgate_passage ntp, nav_tollgate nt, nav_link nl_1, nav_link nl_2, nav_node nn where ntp.tollgate_passage_id = test_feature_id and ntp.toll_id = nt.toll_id and nn.node_id = nt.node_id and nl_1.link_id = nt.in_linkid and nl_2.link_id = nt.out_linkid;"
        rec['nav_lane_connectivity']="select ST_Collect(nl.geom, nn.geom) from nav_lane_connectivity nlc, nav_link nl, nav_node nn where nlc.conn_id =test_feature_id and nn.node_id = nlc.node_id and nl.link_id = nlc.in_linkid;"
        rec['nav_lane_topology']="select ST_Collect(ST_Collect(nl_1.geom, nn.geom), nl_2.geom) from nav_lane_topology nlt, nav_lane_connectivity nlc, nav_link nl_1, nav_link nl_2, nav_node nn where nlt.topo_id =test_feature_id and nlt.conn_id = nlc.conn_id and nn.node_id = nlc.node_id and nl_1.link_id = nlc.in_linkid and nl_2.link_id = nlt.out_linkid;"
        rec['nav_lane_pass']="select nl.geom from nav_link nl, nav_lane_pass nlp where nlp.lane_pass_id =test_feature_id and nlp.link_id = nl.link_id;"
        rec['nav_branch']="select ST_Collect(ST_Collect(nl_1.geom, nn.geom), nl_2.geom) from nav_branch nb, nav_link nl_1, nav_link nl_2, nav_node nn where nb.branch_id =test_feature_id and nn.node_id = nb.node_id and nl_1.link_id = nb.in_linkid and nl_2.link_id = nb.out_linkid;"
        rec['nav_branch_name']="select ST_Collect(ST_Collect(nl_1.geom, nn.geom), nl_2.geom) from nav_branch_name nbn, nav_branch nb, nav_link nl_1, nav_link nl_2, nav_node nn where nbn.branch_name_id =test_feature_id and nbn.branch_id = nb.branch_id and nn.node_id = nb.node_id and nl_1.link_id = nb.in_linkid and nl_2.link_id = nb.out_linkid;"
        rec['nav_branch_pass']="select nl.geom from nav_link nl, nav_branch_pass nbp where nbp.branch_pass_id = test_feature_id and nbp.link_id = nl.link_id;"
        rec['nav_seriesbranch']="select ST_Collect(ST_Collect(nl_1.geom, nn.geom), nl_2.geom) from nav_seriesbranch ns, nav_link nl_1, nav_link nl_2, nav_node nn where ns.series_id = test_feature_id and nn.node_id = ns.node_id and nl_1.link_id = ns.in_linkid and nl_2.link_id = ns.out_linkid;"
        rec['nav_seriesbranch_pass']="select nl.geom from nav_link nl, nav_seriesbranch_pass nsp where nsp.seriesbranch_pass_id =test_feature_id and nsp.link_id = nl.link_id;"
        rec['nav_realimage']="select ST_Collect(ST_Collect(nl_1.geom, nn.geom), nl_2.geom) from nav_realimage nr, nav_link nl_1, nav_link nl_2, nav_node nn where nr.real_id = test_feature_id and nn.node_id = nr.node_id and nl_1.link_id = nr.in_linkid and nl_2.link_id = nr.out_linkid;"
        rec['nav_realimage_pass']="select nl.geom from nav_link nl, nav_realimage_pass nrp where nrp.realimage_pass_id = test_feature_id and nrp.link_id = nl.link_id;"
        rec['nav_sign']="select  ST_Collect(ST_Collect(nl_1.geom, nn.geom), nl_2.geom) from nav_sign ns, nav_link nl_1, nav_link nl_2, nav_node nn where ns.sign_id = test_feature_id and nn.node_id = ns.node_id and nl_1.link_id = ns.in_linkid and nl_2.link_id = ns.out_linkid;"
        rec['nav_sign_name']="select ST_Collect(ST_Collect(nl_1.geom, nn.geom), nl_2.geom) from nav_sign_name nsn, nav_sign ns, nav_link nl_1, nav_link nl_2, nav_node nn where nsn.sign_name_id = test_feature_id and nsn.sign_id = ns.sign_id and nn.node_id = ns.node_id and nl_1.link_id = ns.in_linkid and nl_2.link_id = ns.out_linkid;"
        rec['nav_sign_pass']="select nl.geom from nav_link nl, nav_sign_pass nsp where nsp.sign_pass_id = test_feature_id and nsp.link_id = nl.link_id;"
        rec['nav_restriction']="select ST_Collect(nl.geom, nn.geom) from nav_restriction nr, nav_link nl, nav_node nn where nr.restric_id =test_feature_id and nn.node_id = nr.node_id and nl.link_id = nr.in_linkid;"
        rec['nav_restriction_detail']="select ST_Collect(ST_Collect(nl_1.geom, nn.geom), nl_2.geom) from nav_restriction_detail nrd, nav_restriction nr, nav_link nl_1, nav_link nl_2, nav_node nn where nrd.detail_id =test_feature_id and nrd.restric_id = nr.restric_id and nn.node_id = nr.node_id and nl_1.link_id = nr.in_linkid and nl_2.link_id = nrd.out_linkid;"
        rec['nav_restriction_pass']="select nl.geom from nav_link nl, nav_restriction_pass nrp where nrp.restriction_pass_id = test_feature_id and nrp.link_id = nl.link_id;"
        rec['nav_vspeed']="select ST_Collect(ST_Collect(nl_1.geom, nn.geom), nl_2.geom) from nav_vspeed nv, nav_link nl_1, nav_link nl_2, nav_node nn where nv.vspeed_id =test_feature_id and nn.node_id = nv.node_id and nl_1.link_id = nv.in_link_id and nl_2.link_id = nv.out_link_id;"
        rec['nav_cspeed']="select ST_Collect(nl.geom, nn.geom) from nav_cspeed nc, nav_link nl, nav_node nn where nc.cspeed_id =test_feature_id and nn.node_id = nc.node_id and nl.link_id = nc.link_id;"
        rec['nav_samelink']="select nl.geom from nav_link nl, nav_samelink ns where ns.unik_id = test_feature_id and ns.link_id = nl.link_id;"
        rec['nav_samenode']="select nn.geom from nav_node nn, nav_samenode ns where ns.unik_id = test_feature_id and ns.node_id = nn.node_id;"
        rec['nav_zlevel']="select nav_zlevel.geom from nav_zlevel where  nav_zlevel.zlevel_id = test_feature_id;"
        rec['nav_zlevel_link']="select nz.geom from nav_zlevel nz, nav_zlevel_link nzl where nzl.zlevel_link_id =test_feature_id and nzl.zlevel_id = nz.zlevel_id;"
        rec['nav_cross']="WITH tmp AS (SELECT nc.cross_id, nl.geom from nav_cross nc, nav_cross_link ncl, nav_link nl where nc.cross_id = ncl.cross_id and ncl.link_id = nl.link_id  and nc.cross_id =test_feature_id union all  SELECT nc.cross_id, nn.geom from nav_cross nc, nav_cross_node ncn, nav_node nn where nc.cross_id = ncn.cross_id and ncn.node_id = nn.node_id and nc.cross_id = test_feature_id ) select tmptmp.geom from (select cross_id, ST_Collect(geom) as geom from tmp group by cross_id) as tmptmp where tmptmp.cross_id = test_feature_id;"
        rec['nav_cross_link']="select  nl.geom from nav_cross_link ncl, nav_link nl where ncl.cross_link_id = test_feature_id and ncl.link_id = nl.link_id;"
        rec['nav_cross_node']="select nn.geom from nav_cross_node ncn, nav_node nn where  ncn.cross_node_id =test_feature_id and ncn.node_id = nn.node_id;"
        rec['nav_restriction_cond']="select ST_Collect(ST_Collect(nl_1.geom, nn.geom), nl_2.geom) from nav_restriction_cond nrc, nav_restriction_detail nrd, nav_restriction nr, nav_link nl_1, nav_link nl_2, nav_node nn where nrc.restriction_cond_id =test_feature_id and nrc.detail_id = nrd.detail_id and nrd.restric_id = nr.restric_id and nn.node_id = nr.node_id and nl_1.link_id = nr.in_linkid and nl_2.link_id = nrd.out_linkid;"
        self.sqls=rec

    def Get_Sql(self,Table_Name,Feature_Id):
        Table_Name=Table_Name.lower()
        Feature_Id="'"+Feature_Id+"'"
        self.sql_str=self.sqls[Table_Name].replace('test_feature_id',Feature_Id)
        return self.sql_str
    
if __name__ == "__main__":
    test=Geom()
    sql_test=test.Get_Sql("nav_se","f7af418fc59044d3ba3c6feeb1aebe97")
    print sql_test
