import { Story, Meta } from '@storybook/react/types-6-0';

import { Button, ButtonProps, Colors } from './Button';

export default {
    title: 'Button',
    component: Button
} as Meta;

const Template: Story<ButtonProps> = (args) => <Button {...args}>This is button</Button>;

export const Primary = Template.bind({});
Primary.args = {
    color: Colors.PRIMARY
}

export const Secondary = Template.bind({});
Secondary.args = {
    color: Colors.SECONDARY
}

export const Accent = Template.bind({});
Accent.args = {
    color: Colors.ACCENT
}