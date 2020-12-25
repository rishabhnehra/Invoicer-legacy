import { Story, Meta } from '@storybook/react/types-6-0';

import { Button as ButtonComponent, ButtonProps, Colors } from './Button';

export default {
    title: 'Components/Button',
    component: ButtonComponent,
    argTypes: {
        customColor: { control: 'color' },
        color: {
            control: {
                type: 'radio',
                options: Colors
            }
        }
    }
} as Meta;

const Template: Story<ButtonProps> = (args) => <ButtonComponent {...args}>This is button</ButtonComponent>;

export const Button = Template.bind({});
Button.args = {
    color: Colors.Primary
}