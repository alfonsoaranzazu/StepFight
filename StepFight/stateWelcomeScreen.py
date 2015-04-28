#Welcome Screen
import pygame
from state import State
from button import Button
from buttonListener import ButtonListener
from consts import Consts

class StateWelcomeScreen(State, ButtonListener):
    CONTINUE_BUTTON = 1
    

    def __init__(self, screen, inputManager, character, description):
        State.__init__(self, screen, inputManager)

        self.width, self.height = self.screen.get_width(), self.screen.get_height()
        pygame.display.set_caption("Welcome")

        #Welcome Box Things
        self.activity_description = description
        
        #Fonts
        self.font_object = pygame.font.Font('freesansbold.ttf', 20)


        #Continue Button
        self.continue_button = self._createButton(self.CONTINUE_BUTTON, Consts.CONTINUE, (550,500,300,50))
        self.continue_button.font_object = pygame.font.Font('freesansbold.ttf', 35)
        self.continue_button._setPadding(50, 10)

        self.next_state = Consts.CONTINUE


    def destroy(self):
        self.inputManager.detach(self.continue_button)


    def _createButton(self, button_id, message, rect):
        button = Button(button_id, self, message, Consts.LIGHT_GOLD_COLOR, rect)
        self.inputManager.attach(button)
        button.font_object = self.font_object
        button._setColors(Consts.LIGHT_GOLD_COLOR, Consts.HOVER_GOLD_COLOR, Consts.PRESSED_GOLD_COLOR)

        return button

    def receiveInput(self, event):
        State.receiveInput(self, event)

    def _update(self):
        State._update(self)

        self.continue_button._update()
        return self.next_state

    def _render(self):
        State._render(self)

        self.screen.fill(Consts.LIGHT_GOLD_COLOR)
        self.display_welcome_feedback()
        self.display_activity_description()
        self.display_gold_description()
        self.continue_button._render(self.screen)


    def display_welcome_feedback(self):
        my_font_object = pygame.font.Font('freesansbold.ttf', 50)
        
        feedback = my_font_object.render(Consts.FEEDBACK1, False, Consts.BLACK_COLOR)
        feedback_rect = feedback.get_rect()
        feedback_rect.topleft = (100, 50)
        self.screen.blit(feedback, feedback_rect)

    def display_activity_description(self):
        my_font_object = pygame.font.Font('freesansbold.ttf', 50)

        feedback = my_font_object.render( "' " +self.activity_description+ " '", False, Consts.BLACK_COLOR)
        feedback_rect = feedback.get_rect()
        feedback_rect.topleft = (400, 200)
        self.screen.blit(feedback, feedback_rect)
        
    def display_gold_description(self):
        my_font_object = pygame.font.Font('freesansbold.ttf', 50)

        feedback = my_font_object.render("You received "+str(Consts.MONEY)+" starting Gold!", False, Consts.BLACK_COLOR)
        feedback_rect = feedback.get_rect()
        feedback_rect.topleft = (75, 400)
        self.screen.blit(feedback, feedback_rect)

        

    def clickPerformed(self, button_id):
        if (button_id == self.CONTINUE_BUTTON):
            self.next_state = Consts.STATE_ITEMS_BOARD

        
    
        
        
