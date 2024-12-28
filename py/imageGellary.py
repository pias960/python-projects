from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

class ImageGalleryApp(App):
    def build(self):
        # Main layout for the app
        self.main_layout = BoxLayout(orientation='vertical')

        # Button to add images
        add_image_button = Button(text="Add Images", size_hint=(1, 0.1))
        add_image_button.bind(on_press=self.open_file_chooser)
        self.main_layout.add_widget(add_image_button)

        # Grid layout to display images
        self.image_grid = GridLayout(cols=3, spacing=10, padding=10, size_hint_y=None)
        self.image_grid.bind(minimum_height=self.image_grid.setter('height'))

        # Scrollable view for the grid
        from kivy.uix.scrollview import ScrollView
        scroll_view = ScrollView(size_hint=(1, 0.9))
        scroll_view.add_widget(self.image_grid)

        self.main_layout.add_widget(scroll_view)
        return self.main_layout

    def open_file_chooser(self, instance):
        # File chooser popup
        file_chooser = FileChooserListView(filters=['*.png', '*.jpg', '*.jpeg','*.ico',], path="./")
        popup_layout = BoxLayout(orientation='vertical')
        popup_layout.add_widget(file_chooser)

        # Buttons for popup
        popup_buttons = BoxLayout(size_hint_y=0.1)
        select_button = Button(text="Select")
        cancel_button = Button(text="Cancel")
        popup_buttons.add_widget(select_button)
        popup_buttons.add_widget(cancel_button)
        popup_layout.add_widget(popup_buttons)

        # Create the popup
        self.popup = Popup(title="Select Images", content=popup_layout, size_hint=(0.9, 0.9))

        # Bind buttons
        select_button.bind(on_press=lambda x: self.add_images(file_chooser.selection))
        cancel_button.bind(on_press=self.popup.dismiss)

        self.popup.open()

    def add_images(self, selection):
        # Add selected images to the grid
        for file_path in selection:
            img = AsyncImage(source=file_path, size_hint=(None, None), size=(200, 200))
            self.image_grid.add_widget(img)
        self.popup.dismiss()

if __name__ == "__main__":
    ImageGalleryApp().run()
