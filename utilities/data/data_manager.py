import pandas as pd

class DataManager():
    def __init__(self):
        self.files = {}
        self.files['areas'] = pd.read_csv('tables/areas.csv',index_col='area_id',dtype=str)
        self.files['items'] = pd.read_csv('tables/item_id.csv',index_col='item_id',dtype=str)
        self.files['magics'] = pd.read_csv('tables/magic_id.csv',index_col='magic_id',dtype=str)
        self.files['crystals'] = pd.read_csv('tables/crystal_id.csv',index_col='crystal_id',dtype=str)
        self.files['abilities'] = pd.read_csv('tables/ability_id.csv',index_col='ability_id',dtype=str)
        self.files['gil'] = pd.read_csv('tables/gil_rewards.csv',index_col="gil_id",dtype=str)
        self.files['key_items'] = pd.read_csv('tables/key_items.csv',index_col='keyitem_id',dtype=str)
        self.files['rewards'] = pd.read_csv('tables/rewards.csv', dtype=str)
        self.files['rewards']['idx'] = self.files['rewards']['idx'].astype(int)
        self.files['shops'] = pd.read_csv('tables/shop_id.csv',dtype=str)
        self.files['shops']['idx'] = self.files['shops']['idx'].astype(int)
        self.files['shopprices'] = pd.read_csv('tables/shop_prices.csv', dtype=str)
        self.files['shopprices']['idx'] = self.files['shopprices']['idx'].astype(int)
        self.files['enemies'] = pd.read_csv('tables/enemy_data.csv', dtype=str)
        self.files['enemies_bosses'] = self.files['enemies'][self.files['enemies']['enemy_rank']=='boss']
        self.files['enemies_nonbosses'] = self.files['enemies'][self.files['enemies']['enemy_rank']=='enemy']
        self.files['formations'] = pd.read_csv('tables/formation_id.csv', dtype=str)
        self.files['monsters_in_boxes'] = pd.read_csv('tables/monster_in_a_box.csv',dtype=str)
        self.files['monsters_in_boxes']['monster_box_id'] = self.files['monsters_in_boxes']['monster_box_id'].astype(int)
        self.files['boss_scaling'] = pd.read_csv('tables/boss_scaling.csv')
        self.files['enemy_skills'] = pd.read_csv('tables/enemy_skills.csv',index_col='name').to_dict()['hex']