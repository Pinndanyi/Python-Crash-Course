from get_step import get_step

class RandomWalk():
    """一个生成随机漫步数据的类"""
    
    def __init__(self, num_points = 5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points
        
        #所有随机漫步都始于（0,0）
        self.x_values = [0]
        self.y_values = [0]
    
    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        
        #不断漫步，直到列表到达指定的长度
        while len(self.x_values) < self.num_points:
            
            #决定前进方向及前进的距离
            x_steps = get_step()
            y_steps = get_step()
   
            #拒绝原地踏步
            if x_steps == 0 and y_steps == 0:
                continue
            
            #计算从下一个x和y的值
            next_x = self.x_values[-1] + x_steps
            next_y = self.y_values[-1] + y_steps
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)
            
    