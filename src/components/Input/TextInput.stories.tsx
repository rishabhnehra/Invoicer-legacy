import { Story, Meta } from '@storybook/react/types-6-0';

import { TextInput, TextInputProps } from './TextInput';

export default {
    title: 'Components/Input/Text',
    component: TextInput
} as Meta;

const Template: Story<TextInputProps> = (args) => <TextInput {...args} />;

export const Text = Template.bind({});
Text.args = {
    placeholder: "Email"
}