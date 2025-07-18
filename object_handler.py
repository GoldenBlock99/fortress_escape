from sprite_object import *
from npc import *

class ObjectHandler:
    async def __init__(self,game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/npc/'
        self.static_sprite_path = 'resources/sprites/static_sprites'
        self.anim_sprite_path = 'resources/sprites/animated_sprites'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}

        #sprite map
        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, pos = (1.5, 1.5)))
        add_sprite(AnimatedSprite(game, pos = (1.5, 7.5)))
        add_sprite(AnimatedSprite(game, pos = (5.5, 3.25)))


        #npc map
        add_npc(SoldierNPC(game))
        add_npc(CacoDemonNPC(game, pos = (11.5,4.5)))

    async def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list ]

    async def add_npc(self,npc):
        self.npc_list.append(npc)

    async def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
