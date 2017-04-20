# -*- coding:utf-8 -*-
import tornado
from simpletor import application
from futures import services
from api import Api
from futures.models import Item
from futures.models import Node
from evaluation.models import EvaluationData
from evaluation import services as evaluationService
SUCCESS_ = {"status": "success"}


@application.RequestMapping("/api/item")
class ItemsHandler(application.RequestHandler):
    '''获取标签列表'''

    def get(self):
        items = services.get_items()
        self.render_json(items)

    @Api(auth=True)
    def post(self, *args, **kwargs):
        params = tornado.escape.json_decode(self.request.body)
        item = Item()
        item.name = params['name']
        services.save_item(item)
        self.render_json(SUCCESS_)

    @Api(auth=True)
    def put(self):
        params = tornado.escape.json_decode(self.request.body)
        item_id = params['id']
        services.set_default(item_id)
        self.render_json(SUCCESS_)

    @Api(auth=True)
    def delete(self, *args, **kwargs):
        params = tornado.escape.json_decode(self.request.body)
        item_id = params['id']
        services.remove_item(item_id)
        self.render_json(SUCCESS_)

@application.RequestMapping("/api/item/default")
class DefaultItemHandler(application.RequestHandler):
    def get(self, *args, **kwargs):
        item = services.get_default_item()
        self.render_json(item)

@application.RequestMapping("/api/node")
class NodeHandler(application.RequestHandler):
    def get(self, *args, **kwargs):
        nodes = services.get_nodes()
        self.render_json(nodes)

    @Api(auth=True)
    def post(self, *args, **kwargs):
        params = tornado.escape.json_decode(self.request.body)
        node = Node()
        node.open = params['open']
        node.close = params['close']
        node.highest = params['highest']
        node.lowest = params['lowest']
        node.date = params['ndate']
        node.item_id = params['item']
        services.save_node(node)
        self.render_json(SUCCESS_)

    @Api(auth=True)
    def delete(self, *args, **kwargs):
        params = tornado.escape.json_decode(self.request.body)
        node_id = params['id']
        services.remove_node(node_id)
        self.render_json(SUCCESS_)

@application.RequestMapping("/api/evaluation/data")
class EvaluationDataHandler(application.RequestHandler):
    def get(self, *args, **kwargs):
        dataList = evaluationService.get_all_data()
        self.render_json(dataList)

    def post(self, *args, **kwargs):
        params = tornado.escape.json_decode(self.request.body)
        # print type(params)
        # print params['evaluation_score']
        data = EvaluationData()
        data.trade_date = params['trade_date']
        data.position_time = params['position_time']
        data.profit = params['profit']
        data.commission = params['commission']
        data.evaluation_score = params['evaluation_score']
        evaluationService.save_data(data)
        self.render_json(SUCCESS_)

    def delete(self, *args, **kwargs):
        params = tornado.escape.json_decode(self.request.body)
        data_id = params['id']
        evaluationService.remove_data(data_id)
        self.render_json(SUCCESS_)